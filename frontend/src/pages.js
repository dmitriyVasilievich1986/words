import CreateWordPage from "./components/pages/createWord/CreateWordPage";
import PhrasePage from "./components/pages/phrasePage/PhrasePage";

const PAGES = [
  {
    element: PhrasePage,
    hiden: false,
    name: "HOME",
    path: "/",
  },
  {
    element: CreateWordPage,
    hiden: process.env.NODE_ENV === "production",
    path: "/create",
    name: "CREATE",
  },
];

export default PAGES;
