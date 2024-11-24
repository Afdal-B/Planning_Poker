import React from "react";

const Footer = () => {
  return (
    <footer className="flex-grow bg-neutral-100 text-center p-[22px]">
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
