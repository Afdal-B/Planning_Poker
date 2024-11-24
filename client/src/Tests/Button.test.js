// Button.test.js
import React from "react";
import { render } from "@testing-library/react";
import "@testing-library/jest-dom";
import Button from "./../components/Button";

test("rendu du bouton avec le bon libellé", () => {
  const { getByText } = render(<Button text="Click me" />);
  const buttonElement = getByText("Click me");
  expect(buttonElement).toBeInTheDocument();
});
