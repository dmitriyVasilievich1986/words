import { setState } from "../reducers/wordReducer";
import { useDispatch } from "react-redux";
import Phrase from "./pages/Phrase";
import React from "react";
import axios from "axios";

function App() {
  const dispatch = useDispatch();

  React.useEffect((_) => {
    Promise.all([
      axios.get("/api/verbdeclension/"),
      axios.get("/api/verb/"),
      axios.get("/api/pron/"),
    ])
      .then((values) => {
        const [verbdeclensionData, verbData, pronData] = values;
        dispatch(
          setState({
            verbDeclension: verbdeclensionData.data,
            verb: verbData.data,
            pron: pronData.data,
          })
        );
      })
      .catch((e) => console.log(e));
  }, []);

  return (
    <div>
      <Phrase />
    </div>
  );
}

export default App;
