import React from "react";
import Header from "../components/Header";
import Footer from "../components/Footer";
const InvitationPage = () => {
  const code = localStorage.getItem("room_code");
  return (
    <div>
      <Header></Header>
      <div className="flex items-center justify-center bg-gray-100">
        <div className="w-[600px] bg-gray-100 rounded-lg shadow-lg p-6 m-6">
          <h2 className="text-lg font-semibold text-gray-700 text-center mb-6">
            Invite your team to your room!
          </h2>

          {/* Section "Share this code" */}
          <div className="mb-6">
            <p className="text-sm  mb-2">Share this code</p>
            <div className="flex">
              <input
                type="text"
                value={code}
                readOnly
                className="w-full px-3 py-2 border border-gray-300 bg-white rounded-l-md text-gray-700 focus:outline-none"
              />
              <button className="px-4 py-2 bg-[#378C9FFF] text-white rounded-r-md hover:bg-teal-600">
                Copy
              </button>
            </div>
          </div>

          {/* Section "Share this link" */}
          {/*<div className="mb-6">
            <p className="text-sm  mb-2">Or share this link</p>
            <div className="flex">
              <input
                type="text"
                value="https://www.example.com/lorem_ipsu"
                readOnly
                className="w-full px-3 py-2 border border-gray-300 bg-white rounded-l-md text-gray-700 focus:outline-none"
              />
              <button className="px-4 py-2 bg-[#378C9FFF] text-white rounded-r-md hover:bg-teal-600">
                Copy
              </button>
            </div>
          </div>*/}

          {/* QR Code Section */}
          {/*<div className="flex flex-col items-center mb-6">
            <div className="w-32 h-32 bg-gray-200 flex items-center justify-center rounded-md">
             
              <img
                src="https://via.placeholder.com/128"
                alt="QR Code"
                className="rounded"
              />
            </div>
            <p className="text-2xl mt-2 font-bold">Or share QR code</p>
          </div>*/}

          {/* Bouton de téléchargement */}
          {/*<button className="w-full px-4 py-2 bg-[#378C9FFF] text-white rounded-md hover:bg-teal-600">
            Download
          </button>*/}
        </div>
      </div>
      <Footer></Footer>
    </div>
  );
};

export default InvitationPage;
