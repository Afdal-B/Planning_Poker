import React, { useState } from "react";
import Header from "../components/Header";
import Footer from "../components/Footer";
import FormButton from "../components/FormButton";
import { API_URL } from "../constants/constants";
import axios from "axios";
const UserInfosPage = () => {
  const [displayName, setDisplayName] = useState("");
  const [selectedAvatar, setSelectedAvatar] = useState(null);
  const [code, setCode] = useState("");
  const avatars = [
    {
      id: 1,
      src: "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.disneystore.fr%2Fpersonnages-et-films%2Fpersonnages&psig=AOvVaw1nMCi5CsI7v2fFTMPdXvwe&ust=1734110133091000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCMCRoujdoooDFQAAAAAdAAAAABAR",
      alt: "Avatar 1",
    },
    { id: 2, src: "https://via.placeholder.com/100", alt: "Avatar 2" },
    { id: 3, src: "https://via.placeholder.com/100", alt: "Avatar 3" },
    { id: 4, src: "https://via.placeholder.com/100", alt: "Avatar 4" },
    { id: 5, src: "https://via.placeholder.com/100", alt: "Avatar 5" },
  ];
  const handleSubmit = (e) => {
    e.preventDefault();
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };

    const data = JSON.stringify({
      username: displayName,
      avatar: selectedAvatar,
      room_code: code,
    });
    console.log(data);
    axios
      .post(`${API_URL}/join_room`, data, config) // utilisation des templates strings
      .then((response) => {
        const { room_code, user_id } = response.data; // destructuration de response.data
        console.log(`Room code: ${room_code}, User ID: ${user_id}`);

        // Enregistrement dans le localStorage
        localStorage.setItem("room_code", room_code);
        localStorage.setItem("user_id", user_id);

        // Navigation vers la page de vote
        window.location.href = "/voting";
      })
      .catch((error) => {
        console.error(
          "Erreur lors de la connexion à la room :",
          error.message || error
        );
      });
  };
  return (
    <div>
      <Header></Header>
      <div className="flex items-center justify-center h-[80vh] bg-[#F8F9FAFF]">
        <form onSubmit={handleSubmit}>
          <div className="flex flex-col items-center p-6">
            <h1 className="text-2xl font-bold mb-6 font-archivo">Join Room</h1>
            <div className="w-full max-w-sm">
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Please enter the code provided to you
              </label>
              <input
                type="text"
                placeholder="XUS-K63"
                className="w-full px-4 py-2 mb-6 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                value={code}
                onChange={(e) => setCode(e.target.value)}
              />
            </div>

            <div className="w-full max-w-sm">
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Choose your display name
              </label>
              <input
                type="text"
                value={displayName}
                onChange={(e) => setDisplayName(e.target.value)}
                className="w-full p-2 border border-gray-300 rounded-md focus:ring focus:ring-blue-500 focus:outline-none"
              />
            </div>

            <div className="w-full max-w-sm mt-6 mb-4">
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Choose your avatar
              </label>
              <div className="flex space-x-4">
                {avatars.map((avatar) => (
                  <button
                    key={avatar.id}
                    onClick={() => setSelectedAvatar(avatar.id)}
                    className={`rounded-full border-2 ${
                      selectedAvatar === avatar.id
                        ? "border-blue-500"
                        : "border-transparent"
                    }`}
                  >
                    <img
                      src="https://cdn.pixabay.com/photo/2018/12/03/08/45/snow-3852960_1280.jpg"
                      alt={avatar.alt}
                      className="w-16 h-16 rounded-full"
                    />
                  </button>
                ))}
              </div>
            </div>

            <FormButton text={"Join"}></FormButton>
          </div>
        </form>
      </div>

      <Footer></Footer>
    </div>
  );
};

export default UserInfosPage;
