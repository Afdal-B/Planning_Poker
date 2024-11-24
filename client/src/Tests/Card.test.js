// Card.test.js
import React from "react";
import { render } from "@testing-library/react";
import "@testing-library/jest-dom";
import Card from "./../components/Card";

test("rendu du composant Card avec le bon numéro", () => {
  const { getByText } = render(<Card number={5} />);
  const numberElement = getByText("5");
  expect(numberElement).toBeInTheDocument();
});
