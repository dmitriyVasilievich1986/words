import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Navbar } from "./pages";
import React from "react";

import { CreateWord, UpdateWord } from "./pages/createWord/center";
import CreateWordPage from "./pages/createWord/CreateWordPage";
import PhrasePage from "./pages/phrasePage/PhrasePage";

function App() {
  return (
    <div>
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path="/">
            <Route path="" element={<PhrasePage />} />
            <Route path="create" element={<CreateWordPage />}>
              <Route path="" element={<CreateWord />} />
              <Route path="update/:pk" element={<UpdateWord />} />
            </Route>
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
