import React from "react";
import Card from "./Card";

const Background = () => {
  const generateRandomCards = () => {
    // Générer un nombre aléatoire entre 3 et 5
    const cardCount = Math.floor(Math.random() * 2) + 2;

    // Créer un tableau de cartes avec des styles aléatoires
    return Array.from({ length: cardCount }).map((_, index) => {
      const randomX = Math.random() * 80; // Position horizontale aléatoire (en %)
      const randomY = Math.random() * 80; // Position verticale aléatoire (en %)
      const randomRotation = Math.random() * 60 - 30; // Rotation aléatoire entre -30° et 30°

      return (
        <div
          key={index}
          className="absolute"
          style={{
            left: `${randomX}%`,
            top: `${randomY}%`,
            transform: `rotate(${randomRotation}deg)`,
            zIndex: `1`,
          }}
        >
          <Card number={Math.floor(Math.random() * 5) + 1} />
        </div>
      );
    });
  };

  return (
    <div className="absolute w-full h-screen bg-gray-200">
      {generateRandomCards()}
    </div>
  );
};

export default Background;
