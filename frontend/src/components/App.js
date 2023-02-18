import { BrowserRouter, Route, Routes } from "react-router-dom";
import { setState } from "Reducers/wordReducer";
import { useDispatch } from "react-redux";
import { Navbar } from "./pages";
import PAGES from "Constants";
import React from "react";
import axios from "axios";

function App() {
  const dispatch = useDispatch();
  const [isLoading, setIsLoading] = React.useState(true);

  React.useEffect((_) => {
    Promise.all([
      axios.get("/api/personalPronoun/".toLowerCase()),
      axios.get("/api/nounInfinitive/".toLowerCase()),
      axios.get("/api/verbInfinitive/".toLowerCase()),
      axios.get("/api/randomChoices/".toLowerCase()),
    ])
      .then((values) => {
        const [personalPronoun, nounInfinitive, verbInfinitive, randomChoices] =
          values;
        dispatch(
          setState({
            personalPronoun: personalPronoun.data,
            nounInfinitive: nounInfinitive.data,
            verbInfinitive: verbInfinitive.data,
            randomChoices: randomChoices.data,
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
            {PAGES.map((p) => (
              <Route path={p.path} element={<p.element />} />
            ))}
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
