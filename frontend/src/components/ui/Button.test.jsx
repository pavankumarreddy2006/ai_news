import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import { Button } from "./Button";

describe("Button", () => {
  it("renders content", () => {
    render(<Button>Launch</Button>);
    expect(screen.getByText("Launch")).toBeTruthy();
  });
});
