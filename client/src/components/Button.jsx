import React from "react";
/**
 * Composant Button qui affiche un bouton avec un texte donné.
 *
 * @component
 * @param {Object} props - Les propriétés du composant.
 * @param {string} props.text - Le texte à afficher sur le bouton.
 * @returns {JSX.Element} Le composant Button.
 */
const Button = ({ text, page }) => {
  return (
    <div>
      <button
        className="bg-[#378C9FFF] text-white rounded-[8px] font-serif justify-center p-2 w-60"
        onClick={() => (window.location.href = page)}
      >
        {text}
      </button>
    </div>
  );
};

export default Button;
