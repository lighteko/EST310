import quiz1 from "./assets/image.png";
import quiz2 from "./assets/image copy.png";
import quiz3 from "./assets/image copy 2.png";
import quiz4 from "./assets/image copy 3.png";
import quiz5 from "./assets/image copy 4.png";
import "./App.css";
import Modal from "./Modal";
import { useRef, useState } from "react";

function App() {
  const [modalState, setModalState] = useState(false);
  const currQuiz = useRef({
    quizes: [quiz1, quiz2, quiz3, quiz4, quiz5],
    idx: 0,
  });
  const onClick = () => {
    setModalState(true);
    currQuiz.current.idx++;
    if (currQuiz.current.idx >= 5) currQuiz.current.idx = 0;
  };
  return (
    <footer id="footer">
      {modalState && (
        <Modal
          src={currQuiz.current.quizes[currQuiz.current.idx - 1]}
          setState={setModalState}
        />
      )}
      <div id="camera-button" onClick={onClick}>
        <img
          style={{ width: "80px", height: "80px" }}
          src="./material-symbols-light_camera-outline.svg"
          alt="camera"
        />
      </div>
    </footer>
  );
}

export default App;
