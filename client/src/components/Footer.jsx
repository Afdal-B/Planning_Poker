import React from "react";

/**
 * Composant Footer qui affiche le pied de page de l'application.
 *
 * Ce composant contient un formulaire d'inscription à la newsletter,
 * un sélecteur de langue et des informations de copyright.
 *
 * @param {boolean} classic - Indique si le formulaire de newsletter doit être affiché.
 * @returns {JSX.Element} Le composant Footer.
 */
const Footer = (classic = true) => {
  return (
    <footer className="flex-grow bg-neutral-100 text-center p-[22px]">
      {!classic && (
        <div className="mb-4">
          <form className="space-y-4">
            <label htmlFor="newsletter" className="block text-lg font-medium">
              Subscribe to our newsletter
            </label>
            <input
              type="email"
              id="newsletter"
              name="newsletter"
              placeholder="Enter your email"
              className="w-64 p-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-blue-300"
              required
            />
            <button
              type="submit"
              className="px-4 pt-[10px] pb-[10px] bg-blue-600 text-white rounded-tr-md rounded-br-md hover:bg-blue-700 ml-[-5px] "
            >
              Subscribe
            </button>
          </form>
        </div>
      )}
      <div className="mb-4 text-left">
        <select className="p-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-blue-300">
          <option value="en">English</option>
          <option value="fr">French</option>
        </select>
      </div>
      <div className="text-gray-500 text-sm">&copy; 2024 Brand, Inc.</div>
    </footer>
  );
};

export default Footer;
