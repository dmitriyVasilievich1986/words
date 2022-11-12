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
      axios.get("/api/nouncase/"),
      axios.get("/api/case/"),
      axios.get("/api/noun/"),
    ])
      .then((values) => {
        const [
          verbdeclensionData,
          verbData,
          pronData,
          nounCaseData,
          caseData,
          nounData,
        ] = values;
        dispatch(
          setState({
            verbDeclension: verbdeclensionData.data,
            verb: verbData.data,
            pron: pronData.data,
            nounCase: nounCaseData.data,
            noun: nounData.data,
            case: caseData.data,
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
