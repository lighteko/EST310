import React from "react";

export default function Modal({ src, setState }) {
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
      <button
        onClick={() => {
          setState(false);
        }}
      >
        close
      </button>
    </div>
  );
}
