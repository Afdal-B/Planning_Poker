import React from "react";
import logo from "../assets/icone.png";

/**
 * Composant Header qui affiche le logo et le titre de l'application.
 *
 * Ce composant contient une image de logo et un titre "Planning Poker".
 *
 * @returns {JSX.Element} Le composant Header.
 */
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
