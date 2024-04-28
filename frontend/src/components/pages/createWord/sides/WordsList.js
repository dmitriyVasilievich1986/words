import { useParams, useNavigate } from "react-router-dom";
import { Select } from "../../components";
import classnames from "classnames/bind";
import style from "./style.scss";
import React from "react";
import axios from "axios";

const cx = classnames.bind(style);

function NavigaeItem({ infinitive, partsOfSpeech }) {
  const navigate = useNavigate();
  const params = useParams();

  const isActive =
    params.pk == infinitive.id &&
    partsOfSpeech.find((p) => p.word === params.page).id ===
      infinitive.part_of_speech;

  const clickHandler = () => {
    navigate(`/create/${params.page}/${infinitive.id}`);
  };

  return (
    <div className={cx("navigate-item", { isActive })} onClick={clickHandler}>
      {infinitive.word} / {infinitive.translate}
    </div>
  );
}

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
            <NavigaeItem
              key={infinitive.id}
              infinitive={infinitive}
              partsOfSpeech={partsOfSpeech}
            />
          ))}
      </div>
    </div>
  );
}

export default WordsList;
