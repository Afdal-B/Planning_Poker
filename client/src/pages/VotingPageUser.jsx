import React from "react";
import Timer from "../components/Timer";
import MembersList from "../components/MembersList";
import ChatSection from "../components/ChatSection";
import FeatureListItem from "../components/FeatureListItem";
import Card from "../components/Card";
import axios from "axios";
import { useState, useEffect } from "react";
import { API_URL } from "../constants/constants";
import Chronometer from "../components/Chronometre";
const VotingPageUser = () => {
  const [members, setMembers] = useState([]);
  const [feature, setFeature] = useState({});
  const config = {
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
  return (
    <div className="min-h-screen bg-white">
      <div className="flex h-screen">
        <div className="flex-1 flex flex-col">
          <div className="p-6">
            <Timer></Timer>
          </div>
          <div className="p-6 flex-1 overflow-auto">
            <div className="flex justify-between items-center mb-4">
              <FeatureListItem
                number={""}
                actor={feature.en_tant_que || ""}
                feature={feature.fonctionnalite || ""}
                goal={feature.objectif || ""}
              />
              <div className="flex items-center gap-4">
                <button
                  onClick={fetchCurrentFeature}
                  className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
                >
                  Next Feature
                </button>
              </div>
            </div>
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
