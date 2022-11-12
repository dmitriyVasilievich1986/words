import React from "react";
import axios from "axios";
import { useSelector, useDispatch } from "react-redux";
import { setState } from "../reducers/wordReducer";

function App() {
  const verb = useSelector((state) => state.words.verb);
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

  return <div>App</div>;
}

export default App;
