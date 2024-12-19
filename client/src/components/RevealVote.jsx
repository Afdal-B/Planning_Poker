import React, { useState } from "react";

const RevealVote = () => {
  const votes = [
    { name: "Annie Haley", avatar: "https://via.placeholder.com/50", score: 5 },
    { name: "Annie Haley", avatar: "https://via.placeholder.com/50", score: 2 },
    { name: "Annie Haley", avatar: "https://via.placeholder.com/50", score: 2 },
    { name: "Annie Haley", avatar: "https://via.placeholder.com/50", score: 3 },
    { name: "Annie Haley", avatar: "https://via.placeholder.com/50", score: 1 },
    { name: "Annie Haley", avatar: "https://via.placeholder.com/50", score: 8 },
  ];
  const [reveal, setReveal] = useState(false);
  return (
    <div className="max-w-md mx-auto p-4 bg-white shadow rounded">
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
                    alt={vote.name}
                    className="w-10 h-10 rounded-full"
                  />
                  <div>
                    <p className="text-sm font-medium">{vote.name}</p>
                    <p className="text-xs text-gray-500">Has voted</p>
                  </div>
                </div>
                <span className="text-xl font-bold text-[#378C9FFF]">
                  {vote.score}
                </span>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default RevealVote;
