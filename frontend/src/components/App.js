import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Navbar, PhrasePage, CreateWordPage } from "./pages";
import { setState } from "Reducers/wordReducer";
import { useDispatch } from "react-redux";
import React from "react";
import axios from "axios";

function App() {
  const dispatch = useDispatch();
  const [isLoading, setIsLoading] = React.useState(true);

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
      axios.get("/api/pronoun/"),
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
          pronounData,
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
            pronoun: pronounData.data,
          })
        );
      })
      .catch((e) => console.log(e))
      .finally((_) => setIsLoading(false));
  }, []);

  if (isLoading) return <p>loading...</p>;
  return (
    <div>
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path="/">
            <Route path="" element={<PhrasePage />} />
            <Route path="create" element={<CreateWordPage />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
