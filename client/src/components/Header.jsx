import React from "react";
import logo from "../assets/icone.png";
const Header = () => {
  return (
    <div className="flex flex-row bg-neutral-100 items-center">
      <img
        className="mt-[7px] ml-[20px] w-[40px] h-[40px]"
        src={logo}
        alt="logo"
      />
      <h5 className="mt-[7px] ml-[10px] font-archivo font-bold">
        Planning Poker
      </h5>
    </div>
  );
};

export default Header;
