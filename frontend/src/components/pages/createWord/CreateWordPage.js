import React from "react";
import { useSelector, useDispatch } from "react-redux";
import axios from "axios";

function CreateWordPage() {
  const pron = useSelector((s) => s.words.pron);
  if (pron.length === 0) return null;

  const [newVerb, setNewVerb] = React.useState("");
  const divRef = React.useRef();

  const sendHandler = (_) => {
    const verbWords = newVerb.split(/ |-|\/|\,/);
    const data = {
      verb: { word: verbWords[0], translate: verbWords?.[1] || verbWords[0] },
      verb_pron: [],
    };
    Array.from(divRef.current.children).map((d) => {
      const words = d.value.split(/ |-|\/|\,/);
      data.verb_pron.push({
        pron: d.id,
        word: words[0],
        translate: words?.[1] || words[0],
      });
    });
    axios
      .post("/api/verbdeclension/bulk/", data)
      .then((d) => {
        console.log(d.data);
      })
      .catch((e) => console.log(e));
  };
  return (
    <div>
      <input value={newVerb} onChange={(e) => setNewVerb(e.target.value)} />
      <div ref={divRef}>
        {pron.map((p) => (
          <input key={p.id} id={p.id} placeholder={p.word} />
        ))}
      </div>
      <button onClick={sendHandler}>asd</button>
    </div>
  );
}

export default CreateWordPage;
