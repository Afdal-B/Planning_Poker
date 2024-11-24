import React from "react";

/**
 * Composant Card qui affiche un nombre à l'intérieur d'une carte stylisée.
 *
 * @param {Object} props - Les propriétés du composant.
 * @param {number} props.number - Le nombre à afficher sur la carte.
 * @returns {JSX.Element} Le composant Card.
 */
const Card = ({ number }) => {
  return (
    <div className="flex items-center justify-center w-[40px] h-[60px] bg-gray-100 rounded-lg shadow-lg">
      <h1 className="text-md font-bold text-gray-800">{number}</h1>
    </div>
  );
};

export default Card;
