import React from "react";
import Header from "../components/Header";
import Footer from "../components/Footer";
import { useState } from "react";
import FormButton from "../components/FormButton";
const JoinRoomPage = () => {
  const [code, setCode] = useState("");
  const handleSubmit = () => {};
  return (
    <div>
      <Header></Header>
      <form onSubmit={handleSubmit}>
        <div className="flex items-center justify-center h-[80vh] bg-[#F8F9FAFF]">
          <div className="shadow-md rounded-lg p-8 max-w-sm w-full text-center">
            <h2 className="text-2xl font-bold mb-6 font-archivo">
              Join Existing Room
            </h2>
            <p className="text-gray-600 mb-4">
              Please enter the code provided to you
            </p>
            <input
              type="text"
              placeholder="XUSK63"
              className="w-full px-4 py-2 mb-6 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              value={code}
              onChange={(e) => setCode(e.target.value)}
            />
            <FormButton text={"Join"}></FormButton>
          </div>
        </div>
      </form>
      <Footer></Footer>
    </div>
  );
};

export default JoinRoomPage;
