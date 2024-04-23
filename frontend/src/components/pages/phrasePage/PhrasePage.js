import { useSearchParams } from "react-router-dom";
import { SideContainer } from "../components";
import classnames from "classnames/bind";
import { Select } from "../components";
import PhraseForm from "./PhraseForm";
import style from "./style.scss";
import React from "react";
import axios from "axios";

const cx = classnames.bind(style);

function PhrasePage() {
  const [selectedRules, setSelectedRules] = React.useState([]);
  const [rules, setRules] = React.useState([]);

  const [searchParams, setSearchParams] = useSearchParams();

  React.useEffect(() => {
    axios
      .get("api/rulesrandom/")
      .then((data) => {
        setRules(data.data);
      })
      .catch((e) => console.log(e));
  }, []);

  React.useEffect(() => {
    setSelectedRules(
      searchParams
        .get("rules")
        ?.split(",")
        ?.map((r) => Number(r)) || []
    );
  }, [searchParams.get("rules")]);

  if (rules.length === 0) return <div>Loading...</div>;
  return (
    <div className={cx("page")}>
      <SideContainer className="margin">
        <Select
          multiple={true}
          value={selectedRules}
          options={rules.map((r) => ({ ...r, word: r.name }))}
          onChange={(items) => {
            setSearchParams(items.length > 0 ? { rules: items.join(",") } : {});
            setSelectedRules(items);
          }}
        />
      </SideContainer>
      <div className={cx("center")}>
        <PhraseForm selectedRules={selectedRules} rules={rules} />
      </div>
      <div className={cx("side")} />
    </div>
  );
}

export default PhrasePage;
