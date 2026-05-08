/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        night: "#060816",
        glow: "#67b7ff",
        violetGlow: "#8d78ff",
        panel: "rgba(10,15,32,0.7)",
      },
      boxShadow: {
        glow: "0 0 0 1px rgba(103,183,255,0.18), 0 10px 40px rgba(54,118,255,0.18)",
      },
      backgroundImage: {
        grid: "linear-gradient(rgba(255,255,255,0.04) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.04) 1px, transparent 1px)",
      },
    },
  },
  plugins: [],
};

