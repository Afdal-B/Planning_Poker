import React from "react";

const Button = ({ text }) => {
  return (
    <div>
      <button className="bg-[#378C9FFF] text-white rounded-[8px] font-serif justify-center p-2 w-60">
        {text}
      </button>
    </div>
  );
};

export default Button;
