import React, { useState, useEffect } from "react";
import MembersList from "../components/MembersList";
import ChatSection from "../components/ChatSection";
import BacklogTable from "../components/BacklogTable";
import axios from "axios";
import { API_URL } from "../constants/constants";
const VotingPage = () => {
  const [items, setItems] = useState([]);
  const [members, setMembers] = useState([]);
  const config = {
    headers: {
      "Content-Type": "application/json",
    },
  };

  useEffect(() => {
    const fetchBacklog = () => {
      try {
        axios
          .post(
            API_URL + "/backlog",
            JSON.stringify({ room_code: localStorage.getItem("room_code") }),
            config
          )
          .then((response) => {
            console.log(response.data.tasks);
            setItems(response.data.tasks);
          });
      } catch (error) {
        console.error("Erreur lors de la récupération du backlog:", error);
      }
    };

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

    fetchBacklog();
    fetchMembers();
  }, []);

  return (
    <div className="min-h-screen bg-white">
      <div className="flex h-screen">
        <div className="flex-1 flex flex-col">
          <div className="p-6 flex-1 overflow-auto">
            <BacklogTable backlogItems={items} />
          </div>
        </div>
        <div className="w-80 flex flex-col border-l">
          <MembersList members={members || []} />
          <ChatSection />
        </div>
      </div>
    </div>
  );
};

export default VotingPage;
