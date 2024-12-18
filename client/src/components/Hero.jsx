import React from "react";
import Button from "./Button";
import Background from "./Background";

/**
 * Composant Hero qui affiche la section principale de l'application.
 *
 * Ce composant contient un titre, une description et deux boutons
 * permettant à l'utilisateur de créer ou de rejoindre une salle.
 *
 * @returns {JSX.Element} Le composant Hero.
 */
const Hero = () => {
  return (
    <div className="flex flex-col items-center pt-28 pb-28 bg-[#F8F9FAFF] h-[80vh]">
      <h2 className="font-archivo font-bold text-3xl mb-3 z-10">
        Collaborate and streamline
      </h2>
      <p className="font-light text-sm">
        Efficiently plan and estimate tasks with ease
      </p>
      <div className="flex flex-row gap-6 mt-6">
        <Button text={"Create Room"} page={"/create-room"}></Button>
        <Button text={"Join Existing Room"} page={"/profile"}></Button>
      </div>
    </div>
  );
};

export default Hero;
