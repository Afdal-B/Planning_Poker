import React from "react";

const Card = ({ number, width, height }) => {
  return (
    <div className="flex items-center justify-center w-[40px] h-[60px] bg-gray-100 rounded-lg shadow-lg">
      <h1 className="text-md font-bold text-gray-800">{number}</h1>
    </div>
  );
};

export default Card;
