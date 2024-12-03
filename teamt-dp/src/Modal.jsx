import React, { useState } from "react";

export default function Modal({ src, setState, setQuiz, quiz }) {
  const answers = ["heart, angel", "strawberry fields", "love, peace", "A", "D"]
  const [input, setInput] = useState("");
  return (
    <div
      style={{
        width: "100vw",
        height: "40vh",
        marginBottom: "80vh",
      }}
    >
      <img
        style={{
          width: "100vw",
        }}
        src={src}
        alt="quiz"
      />
      <input value={input} onChange={(e) => setInput(e.target.value)} />
      <button
        onClick={() => {
          if (input !== answers[quiz]) {
            alert("Wrong! The answer was: " + answers[quiz]);
          } else {
            alert("Correct!");
          }
          setQuiz(quiz + 1 < 5 ? quiz + 1 : 0);
          setState(false);
        }}
      >
        submit
      </button>
    </div>
  );
}
