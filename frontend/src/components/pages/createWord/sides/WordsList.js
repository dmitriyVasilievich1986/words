import { NavLink, useParams, useNavigate } from "react-router-dom";
import { Select } from "../../components";
import classnames from "classnames/bind";
import style from "./style.scss";
import React from "react";
import axios from "axios";

const cx = classnames.bind(style);

function WordsList({ infinitives }) {
  const [partsOfSpeech, setPartsOfSpeech] = React.useState([]);
  const [search, setSearch] = React.useState("");

  const navigate = useNavigate();
  const params = useParams();

  React.useEffect(() => {
    axios
      .get("/api/partsofspeech/")
      .then((response) => {
        setPartsOfSpeech(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  React.useEffect(() => {
    if (!params?.page && partsOfSpeech.length > 0) {
      navigate(`/create/${partsOfSpeech[0].word.toLowerCase()}/`);
    }
  }, [params.page, partsOfSpeech]);

  if (partsOfSpeech.length === 0) return null;
  return (
    <div className={cx("list")}>
      <div style={{ marginBottom: "2rem", width: "180px" }}>
        <Select
          options={partsOfSpeech.map((p) => ({ ...p, word: p.translate }))}
          onChange={(p) => navigate(`/create/${p.word.toLowerCase()}/`)}
          isNullable={false}
          value={
            partsOfSpeech.find((p) => p.word.toLowerCase() === params.page)?.id
          }
        />
      </div>
      <div className={cx("search")}>
        <input
          type="text"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
      </div>
      <div className={cx("wrapper")}>
        {infinitives
          .filter(
            (i) =>
              search === "" ||
              i.word.toLowerCase().includes(search.toLowerCase()) ||
              i.translate.toLowerCase().includes(search.toLowerCase())
          )
          .map((infinitive) => (
            <div key={infinitive.id}>
              <NavLink
                className={({ isActive }) => cx({ isActive })}
                to={`/create/${partsOfSpeech
                  .find((p) => p.id == infinitive.part_of_speech)
                  .word.toLowerCase()}/${infinitive.id}`}
              >
                {infinitive.word} / {infinitive.translate}
              </NavLink>
            </div>
          ))}
      </div>
    </div>
  );
}

export default WordsList;
