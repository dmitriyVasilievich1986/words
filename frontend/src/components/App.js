import { BrowserRouter, Route, Routes } from "react-router-dom";
import { setState } from "Reducers/wordReducer";
import { useDispatch } from "react-redux";
import PAGES from "./pages/Routes";
import { Navbar } from "./pages";
import React from "react";
import axios from "axios";

function App() {
  const dispatch = useDispatch();
  const [isLoading, setIsLoading] = React.useState(true);

  React.useEffect((_) => {
    Promise.all([
      axios.get("/api/personalpronoun/"),
      axios.get("/api/nouninfinitive/"),
      axios.get("/api/verbinfinitive/"),
      axios.get("/api/declentions/"),
      axios.get("/api/gender/"),
    ])
      .then((values) => {
        const [
          personalPronoun,
          nounInfinitive,
          verbInfinitive,
          declentions,
          gender,
        ] = values;
        dispatch(
          setState({
            personalPronoun: personalPronoun.data,
            nounInfinitive: nounInfinitive.data,
            verbInfinitive: verbInfinitive.data,
            declentions: declentions.data,
            gender: gender.data,
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
