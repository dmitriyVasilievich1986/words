import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Navbar } from "./pages";
import PAGES from "Pages";
import React from "react";

function App() {
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
