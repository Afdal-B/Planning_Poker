import React from "react";
import Header from "../components/Header";
import Footer from "../components/Footer";
import FormButton from "../components/FormButton";
import { useState } from "react";
import axios from "axios";
import { API_URL } from "../constants/constants";
const CreateRoomPage = () => {
  const [roomName, setRoomName] = useState("");
  const [gameRule, setGameRule] = useState("");
  const [jsonFile, setJsonFile] = useState(null);
  const [pseudo, setPseudo] = useState("");
  const [avatar, setAvatar] = useState("");
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();
    if (file && file.type === "application/json") {
      reader.onload = (e) => {
        if (file && file.type === "application/json") {
          try {
            setJsonFile(e.target.result);
          } catch (error) {
            console.error("invalid json");
          }
        }
      };
      reader.readAsText(file);
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };

    const data = JSON.stringify({
      room_name: roomName,
      game_rule: gameRule,
      backlog_json: jsonFile,
      username_creator: pseudo,
      avatar_creator: avatar,
    });
    console.log(data);
    axios.post(API_URL + "/create_room", data, config);
  };
  return (
    <div>
      <Header></Header>
      <div className="flex items-center justify-center min-h-[80vh] bg-[#F8F9FAFF]">
        <form className="p-6 rounded-lg shadow-lg w-96" onSubmit={handleSubmit}>
          <h1 className="text-2xl font-bold text-gray-800 text-center mb-6 font-archivo">
            Create Room
          </h1>

          {/* Room Name */}
          <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Enter the room's name
            </label>
            <input
              type="text"
              value={roomName}
              onChange={(e) => setRoomName(e.target.value)}
              placeholder="Planning poker project"
              className="w-full px-4 py-2 border rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Enter your pseudo
            </label>
            <input
              type="text"
              value={pseudo}
              onChange={(e) => setPseudo(e.target.value)}
              placeholder="pseudo"
              className="w-full px-4 py-2 border rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Avatar
            </label>
            <input
              type="text"
              value={avatar}
              onChange={(e) => setAvatar(e.target.value)}
              placeholder="avatar"
              className="w-full px-4 py-2 border rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          {/* Game Rule */}
          <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Choose the game's rule
            </label>
            <select
              value={gameRule}
              onChange={(e) => setGameRule(e.target.value)}
              className="w-full px-4 py-2 border rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="">Select a rule</option>
              <option value="strict">Strict</option>
              <option value="moyenne">Moyenne</option>
            </select>
          </div>

          {/* Import JSON */}
          <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Import your backlog in JSON format
            </label>
            <div className="relative mb-4">
              <input
                type="file"
                accept=".json"
                onChange={handleFileChange}
                className="hidden"
                id="jsonFile"
              />
              <input
                type="text"
                placeholder="Click on the import icon"
                className="w-full px-4 py-2 border rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
                readOnly
                value={jsonFile ? jsonFile.name : ""}
              />
              <label
                htmlFor="jsonFile"
                className="absolute right-2 top-1/2 transform -translate-y-1/2 cursor-pointer"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-5 w-5 text-gray-700 hover:text-gray-900"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M12 4v16m8-8H4"
                  />
                </svg>
              </label>
            </div>
          </div>

          {/* Submit Button */}
          <FormButton text={"Create"}></FormButton>
        </form>
      </div>
      <Footer></Footer>
    </div>
  );
};

export default CreateRoomPage;
