import React from "react";
import Timer from "../components/Timer";
import MembersList from "../components/MembersList";
import ChatSection from "../components/ChatSection";
import FeatureListItem from "../components/FeatureListItem";
import Card from "../components/Card";
import axios from "axios";
import { useState, useEffect } from "react";
import {io} from "socket.io-client";
import { API_URL } from "../constants/constants";
import RevealVote from "../components/RevealVote";
const VotingPageUser = () => {
  const [members, setMembers] = useState([]);
  const [feature, setFeature] = useState({});
  const socket = io(API_URL);
  const handleVote =()=>{
    axios.post(API_URL+"/vote",JSON.stringify({round_id:localStorage.getItem("round_id"),user_id,vote_value}))
  }
  socket.on("connect", () => {
    console.log('Réussi');
  });
  
  useEffect(() => {
    // Écouter l'événement 'round_created' pour afficher les données
    socket.on('round_created', (data) => {
      console.log('Round Created:', data);
      setFeature(data.task);
      localStorage.setItem("room_id",data.round_id)
    });
    const intervalId = setInterval(() => {
      socket.emit('members', { room_code: localStorage.getItem("room_code") })
    }, 2000); 
    //socket.emit('members', { room_code: localStorage.getItem("room_code") })
    socket.on("get_members",(data)=>{
      console.log(data)
      setMembers(data.members)
    })
    // Écouter les erreurs
    socket.on('error', (error) => {
      console.error('Error:', error.message);
    });

    return () => {
      socket.off('round_created');
      socket.off('error');
    };
   return () => clearInterval(intervalId)
  }, []);

  const handleCreateRound = () => {
    // Émettre l'événement 'create_round'
    socket.emit('create_round', { room_code: localStorage.getItem("room_code") });

  };
  
  /*const config = {
    headers: {
      "Content-Type": "application/json",
    },
  };

  const fetchCurrentFeature = () => {
    try {
      axios
        .post(
          API_URL + "/round",
          JSON.stringify({ room_code: localStorage.getItem("room_code") }),
          config
        )
        .then((response) => {
          console.log(response.data.feature);
          localStorage.setItem("round_id", response.data.room_id);
          setFeature(response.data.task);
        });
    } catch (error) {
      console.error("Erreur lors de la récupération de la feature:", error);
    }
  };

  useEffect(() => {
    const fetchMembers = () => {
      try {
        axios
          .post(
            API_URL + "/users",
            JSON.stringify({ room_code: localStorage.getItem("room_code") }),
            config
          )
          .then((response) => {
            console.log(response.data.users);
            setMembers(response.data.users);
          });
      } catch (error) {
        console.error("Erreur lors de la récupération des users:", error);
      }
    };

    fetchMembers();
    fetchCurrentFeature();
  }, []);
  */
  return (
    <div className="min-h-screen bg-white">
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
              <FeatureListItem
                number={""}
                actor={feature.en_tant_que || ""}
                feature={feature.fonctionnalite || ""}
                goal={feature.objectif || ""}
              />
              <div className="absolute right-[20px] ">
                <button
                  onClick={handleCreateRound}
                  className="bg-[#378C9FFF] text-white px-4 py-2 rounded hover:bg-[#1b5764] "
                >
                  Next
                </button>
              </div>
            </div>
            <RevealVote></RevealVote>
          </div>
          <div>
            <button
            onClick={handleVote}
            >Vote</button>
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
            <Card number="café" />
            <Card number="?" />
          </div>
        </div>
        <div className="w-80 flex flex-col border-l">
          <MembersList members={members} />
          <ChatSection />
        </div>
      </div>
    </div>
  );
};

export default VotingPageUser;
