import React from "react";

/**
 * Composant FormButton qui affiche un bouton de soumission avec un texte donné.
 *
 * @component
 * @param {Object} props - Les propriétés du composant.
 * @param {string} props.text - Le texte à afficher sur le bouton.
 * @returns {JSX.Element} Le composant FormButton.
 */
const FormButton = ({ text }) => {
  return (
    <button
      type="submit"
      className="w-full bg-[#378C9FFF] text-white py-2 px-4 rounded-lg hover:bg-[#1b5764] focus:ring-2 focus:ring-[#a7d3dd] focus:ring-offset-1"
    >
      {text}
    </button>
  );
};

export default FormButton;
