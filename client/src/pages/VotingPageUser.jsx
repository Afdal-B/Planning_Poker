import React from "react";
import Timer from "../components/Timer";
import MembersList from "../components/MembersList";
import ChatSection from "../components/ChatSection";
import FeatureListItem from "../components/FeatureListItem";
import Card from "../components/Card";
import { useState, useEffect } from "react";
import { io } from "socket.io-client";
import { API_URL} from "../constants/constants";
import RevealVote from "../components/RevealVote";
import TaskEstimated from "../components/TaskEstimated";
import socket from "../components/Socket";
const VotingPageUser = () => {
  const [members, setMembers] = useState([]);
  const [feature, setFeature] = useState({});
  const [estimated, setEstimated] = useState(false);
  const [votes, setVotes] = useState([]);
  const [estimation, setEstimation] = useState("");
  const [nextButton, setNextButton] = useState(true);
  const [taskEstmatedModal, setTaskEstimatedModal] = useState(false);
  const [messages,setMessages] = useState([]);
  let hasVoted = false;
  socket.on("connect", () => {
    console.log("connexion réussie");
  });
  /*const handleDownload = () => {
    try {
      // Appel à l'API pour récupérer le fichier JSON
      axios
        .get(API_URL + "/download-json", {
          responseType: "blob", // Nécessaire pour traiter la réponse comme un fichier
        })
        .then((response) => {
          console.log("fichier", response.data);
          const url = window.URL.createObjectURL(response.data);
          // Création d'un élément <a> pour télécharger le fichier
          const a = document.createElement("a");
          a.href = url;
          a.download = "backlog_temporaire.json"; // Nom du fichier
          document.body.appendChild(a);
          a.click();
          a.remove();
        })
        .catch((error) => {
          console.log(error);
        });

      // Création d'un blob à partir de la réponse
      //const blob = new Blob([response.data], { type: 'application/json' });
    } catch (error) {
      console.error("Erreur lors du téléchargement du fichier JSON:", error);
    }
  };*/
  /*const config = {
    headers: {
      "Content-Type": "application/json",
    },
  };*/
  const handleRevealVote=()=>{
    socket.emit("reveal_votes", {
      round_id: localStorage.getItem("round_id"),
      room_code: localStorage.getItem("room_code"),
    });
  }
  const handleChatMessage = () => {
    const data =  {
      user_id: localStorage.getItem("user_id"),
      room_code: localStorage.getItem("room_code"),
      message: localStorage.getItem("message"),
    }
    console.log("emitting message",data);
    socket.emit("send_message",data);
  }
  const handleVote = () => {
    // Préparer les données pour l'événement
    const data = {
      round_id: localStorage.getItem("round_id"),
      user_id: localStorage.getItem("user_id"),
      vote_value: localStorage.getItem("vote"),
    };
  
    console.log(data);
  
    // Émettre un événement de vote au serveur
    socket.emit("vote", data, (response) => {
      // Callback pour gérer la réponse du serveur
      if (response.success) {
        console.log("Succès du vote");
      } else {
        console.log("Erreur lors du vote :", response.error);
      }
    });
  
    // Mettre à jour l'état de vote
    hasVoted = true;
  };
  
  // Gérer la connexion au serveur Socket.IO
  socket.on("connect", () => {
    console.log("Connexion réussie au serveur Socket.IO");
  });
  
  // Gérer les erreurs de connexion
  socket.on("connect_error", (error) => {
    console.error("Erreur de connexion à Socket.IO :", error);
  });

  const handleCreateRound = () => {
    // Émettre l'événement 'create_round'
    socket.emit("create_round", {
      room_code: localStorage.getItem("room_code"),
    });
    console.log("create round emitted")
    hasVoted = false;
  };
  
  useEffect(() => {
    handleCreateRound()
    // Écouter l'événement 'round_created' pour afficher les données
    socket.on("round_created", (data) => {
      console.log("Round Created:", data);

      setFeature(data.task);
      localStorage.setItem("round_id", data.round_id);
    });
    socket.on("get_users_votes", (data) => {
      console.log("votes des utilisateurs", data.votes);
      setVotes(data.votes);
    });

    socket.on("get_reveal_votes", (data) => {
      console.log("estimation", data);
      setEstimated(data.estimated);
      if (data.estimated) {
        console.log(String(data.estimation))
        setEstimation(String(data.estimation));
      }
    });
    socket.on("new_message", (data) => {
      console.log("new message reçu", data);
       setMessages(data);
   });

   socket.emit('chat_history',{room_code:localStorage.getItem("room_code")});
   socket.on('chat_history_response',(data)=>{
    console.log("chat history reçu",data);
    setMessages(data);
   })
    const intervalId = setInterval(() => {
      socket.emit("members", { room_code: localStorage.getItem("room_code") });
      
    }, 3000);
    //socket.emit('members', { room_code: localStorage.getItem("room_code") })
    socket.on("get_members", (data) => {
      console.log(data);
      setMembers(data.members);
    });
    // Écouter les erreurs
    socket.on("error", (error) => {
      console.error("Error:", error.message);
    });

    return () => {
      socket.off("round_created");
      socket.off("error");
      clearInterval(intervalId);
    };
  }, []);

 
  return (
    <div className="min-h-screen bg-white">
      <TaskEstimated
        isOpen={taskEstmatedModal}
        onClose={() => setTaskEstimatedModal(false)}
        difficulty={estimation}
        onNextTask={handleCreateRound}
      />
      <div className="flex h-screen">
        <div className="flex flex-col">
          <div className="flex justify-between p-5">
            <h1 className="text-2xl font-bold">Room Name</h1>
            <div>
              <Timer></Timer>
            </div>
          </div>
          <div className="p-6 flex-1 overflow-auto">
            <div className="relative flex justify-center items-center mb-4">
              {!hasVoted && (
                <FeatureListItem
                  number={""}
                  actor={feature.en_tant_que || ""}
                  feature={feature.fonctionnalite || ""}
                  goal={feature.objectif || ""}
                />
              )}
              <div className="absolute right-[10px]">
                <button
                className="bg-[#378C9FFF] text-white px-4 py-2 rounded hover:bg-[#1b5764]"

                onClick={handleCreateRound}
                >
                  Next
                </button>
              </div>
            </div>
            
          </div>
          <div className="flex w-[100%] items-center justify-center mt-[2px] gap-4">
          <button
              onClick={() => {
                socket.emit("users_votes", {
                  round_id: localStorage.getItem("round_id"),
                  room_code: localStorage.getItem("room_code"),
                });
              }}
            >
              <RevealVote
                votes={votes}
                OnShowEstimation={() => {
                  socket.emit("reveal_votes", {
                    round_id: localStorage.getItem("round_id"),
                    room_code: localStorage.getItem("room_code"),
                  });
                  setTaskEstimatedModal(true);
                }}
              ></RevealVote>
            </button>
            <button
              onClick={handleVote}
              className="bg-[#378C9FFF] text-white px-4 py-2 rounded hover:bg-[#1b5764] mt-4"
            >
              Vote
            </button>
          </div>
          <div className="flex gap-6 p-6 border-t">
            <Card number="1" />
            <Card number="2" />
            <Card number="3" />
            <Card number="5" />
            <Card number="8" />
            <Card number="13" />
            <Card number="20" />
            <Card number="40" />
            <Card number="100" />
            <Card number="coffee" />
            <Card number="?" />
          </div>
        </div>
        <div className="w-80 flex flex-col border-l">
          <MembersList members={members} />
          <ChatSection messages = {messages} handleSend={handleChatMessage}/>
        </div>
      </div>
    </div>
  );
};

export default VotingPageUser;
