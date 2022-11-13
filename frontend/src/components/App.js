import PhrasePage from "./pages/phrasePage/PhrasePage";
import { setState } from "../reducers/wordReducer";
import { useDispatch } from "react-redux";
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
      axios.get("/api/adjective/"),
      axios.get("/api/adjcase/"),
    ])
      .then((values) => {
        const [
          verbdeclensionData,
          verbData,
          pronData,
          nounCaseData,
          caseData,
          nounData,
          adjectiveData,
          adjcaseData,
        ] = values;
        dispatch(
          setState({
            verbDeclension: verbdeclensionData.data,
            verb: verbData.data,
            pron: pronData.data,
            nounCase: nounCaseData.data,
            noun: nounData.data,
            case: caseData.data,
            adjective: adjectiveData.data,
            adjCase: adjcaseData.data,
          })
        );
      })
      .catch((e) => console.log(e));
  }, []);

  return (
    <div>
      <PhrasePage />
    </div>
  );
}

export default App;
