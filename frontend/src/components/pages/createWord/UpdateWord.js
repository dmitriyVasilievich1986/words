import className from "classnames";
import style from "./style.scss";
import React from "react";
import axios from "axios";

const cx = className.bind(style);

function UpdateWord(props) {
  const [personal_pronouns, setPersonal_pronouns] = React.useState([]);
  const [infinitive, setInfinitive] = React.useState(null);
  const [isLoading, setIsLoading] = React.useState(0);

  React.useEffect(() => {
    setIsLoading((prev) => prev + 1);
    Promise.all([
      axios.get(`/api/infinitive/${props.pk}/`),
      axios.get("/api/personal_pronoun/"),
      axios.post(`/api/verb/infinitive/`, { infinitive: props.pk }),
    ])
      .then((response) => {
        const [infinitive, personal_pronouns, verbs] = response;
        const ppVerb = personal_pronouns.data.map((pp) => {
          const verb = verbs.data.find((v) => v.personal_pronoun === pp.id) || {
            word: "",
            translate: "",
          };
          return [pp.id, verb];
        });
        setInfinitive({
          ...infinitive.data,
          ppVerbs: Object.fromEntries(ppVerb),
        });
        setPersonal_pronouns(personal_pronouns.data);
      })
      .catch((error) => {
        console.log(error);
      })
      .finally((_) => {
        setIsLoading((prev) => prev - 1);
      });
  }, [props.pk]);

  const submitHandler = () => {
    Object.keys(infinitive.ppVerbs).forEach((ppId) => {
      if (
        infinitive.ppVerbs[ppId].translate === "" ||
        infinitive.ppVerbs[ppId].word === ""
      )
        return;
      setIsLoading((prev) => prev + 1);

      axios({
        method: infinitive.ppVerbs[ppId].id ? "put" : "post",
        url: infinitive.ppVerbs[ppId].id
          ? `/api/verb/${infinitive.ppVerbs[ppId].id}/`
          : "/api/verb/",
        data: {
          ...infinitive.ppVerbs[ppId],
          infinitive: props.pk,
          personal_pronoun: ppId,
        },
      })
        .then((response) => {
          setInfinitive((prev) => {
            const ppVerbs = { ...prev.ppVerbs };
            ppVerbs[response.data.personal_pronoun] = response.data;
            return { ...prev, ppVerbs };
          });
        })
        .catch((error) => {
          console.log(error);
        })
        .finally((_) => {
          setIsLoading((prev) => prev - 1);
        });
    });
  };

  const uodatePPVerb = ({ name, value }, ppId) => {
    setInfinitive((prev) => {
      const ppVerbs = { ...prev.ppVerbs };
      ppVerbs[ppId] = { ...ppVerbs[ppId], [name]: value };
      return { ...prev, ppVerbs };
    });
  };

  if (isLoading > 0) return <div>loading...</div>;
  return (
    <div className={cx("container")}>
      <form onSubmit={submitHandler}>
        {personal_pronouns.map((personal_pronoun) => {
          const verb = infinitive.ppVerbs[personal_pronoun.id];
          return (
            <div
              key={personal_pronoun.id}
              className={cx("input-wrapper")}
              style={{ marginTop: "5px" }}
            >
              <div className={cx("input-row")}>
                <label>{personal_pronoun.word}</label>
                <input
                  type="text"
                  name="word"
                  placeholder="word"
                  value={verb.word}
                  onChange={(e) => uodatePPVerb(e.target, personal_pronoun.id)}
                />
              </div>
              <div className={cx("input-row")}>
                <label>{personal_pronoun.translate}</label>
                <input
                  type="text"
                  name="translate"
                  placeholder="translate"
                  value={verb.translate}
                  onChange={(e) => uodatePPVerb(e.target, personal_pronoun.id)}
                />
              </div>
            </div>
          );
        })}
        <div className={cx("send-button")}>
          <button>send</button>
        </div>
      </form>
    </div>
  );
}

export default UpdateWord;
