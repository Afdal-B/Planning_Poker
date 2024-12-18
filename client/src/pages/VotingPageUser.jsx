import React from "react";
import Timer from "../components/Timer";
import MembersList from "../components/MembersList";
import ChatSection from "../components/ChatSection";
import FeatureListItem from "../components/FeatureListItem";
import Card from "../components/Card";
import axios from "axios";
import { useState, useEffect } from "react";
import { API_URL } from "../constants/constants";
const VotingPageUser = () => {
  const [members, setMembers] = useState([]);

  useEffect(() => {
    const fetchMembers = () => {
      try {
        const response = axios.post(
          API_URL + "/members",
          JSON.stringify({ room_code: localStorage.getItem("room_code") })
        );
        setMembers(response.data);
      } catch (error) {
        console.error("Erreur lors de la récupération des membres:", error);
      }
    };

    fetchMembers();
  }, []);
  return (
    <div className="min-h-screen bg-white">
      <div className="flex h-screen">
        <div className="flex-1 flex flex-col">
          <div className="p-6 flex-1 overflow-auto">
            <FeatureListItem
              number="03"
              actor="User"
              feature="Create an account"
              goal="Acces the platform"
            />
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
