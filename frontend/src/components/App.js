import { BrowserRouter, Route, Routes } from "react-router-dom";
import { setState } from "Reducers/wordReducer";
import { useDispatch } from "react-redux";
import { Navbar } from "./pages";
import PAGES from "Pages";
import React from "react";
import axios from "axios";

function App() {
  const dispatch = useDispatch();
  const [isLoading, setIsLoading] = React.useState(true);

  React.useEffect((_) => {
    axios
      .get("/api/randomChoices/".toLowerCase())
      .then((data) => {
        dispatch(setState({ randomChoices: data.data }));
      })
      .catch((e) => {
        console.log(e);
      })
      .finally((_) => {
        setIsLoading(false);
      });
  }, []);

  if (isLoading) return <p>loading...</p>;
  return (
    <div>
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path="/">
            {PAGES.map((p) => (
              <Route path={p.path} key={p.name} element={<p.element />} />
            ))}
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
