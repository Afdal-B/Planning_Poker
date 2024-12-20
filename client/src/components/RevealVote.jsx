import React, { useState } from "react";

const RevealVote = ({ votes, OnShowEstimation }) => {
  const [reveal, setReveal] = useState(false);
  return (
    <div className="w-[300px] mx-auto p-4 bg-white shadow rounded">
      <button
        className="mt-4 w-full bg-[#378C9FFF] text-white py-2 rounded "
        onClick={() => {
          setReveal(!reveal);
        }}
      >
        Reveal
      </button>
      {reveal && (
        <div>
          <h2 className="text-lg font-semibold mb-4 text-center">Votes</h2>
          <ul className="space-y-4">
            {votes.map((vote, index) => (
              <li
                key={index}
                className="flex items-center justify-between bg-gray-50 p-3 rounded shadow-sm"
              >
                <div className="flex items-center space-x-3">
                  <img
                    src={vote.avatar}
                    alt={vote.username}
                    className="w-10 h-10 rounded-full"
                  />
                  <div>
                    <p className="text-sm font-medium">{vote.username}</p>
                    <p className="text-xs text-gray-500">Has voted</p>
                  </div>
                </div>
                <span className="text-xl font-bold text-[#378C9FFF]">
                  {vote.vote_value}
                </span>
              </li>
            ))}
          </ul>
          <button
            onClick={OnShowEstimation}
            className="bg-[#378C9FFF] text-white px-4 py-2 rounded hover:bg-[#1b5764]"
          >
            show estimation
          </button>
        </div>
      )}
    </div>
  );
};

export default RevealVote;
