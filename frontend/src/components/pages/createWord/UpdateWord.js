import classnames from "classnames/bind";
import style from "./style.scss";
import React from "react";
import axios from "axios";

const cx = classnames.bind(style);

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
        props.setTags(infinitive.data.tags.map((t) => t.tags));
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
    setIsLoading((prev) => prev + 1);
    axios
      .put(`/api/infinitive/${props.pk}/`, {
        ...infinitive,
        part_of_speech: infinitive.part_of_speech.id,
        tags: props.tags,
      })
      .then((response) => {
        setInfinitive((prev) => ({ ...prev, ...response.data }));
        props.setInfinitives((prev) =>
          prev.map((inf) => (inf.id === response.data.id ? response.data : inf))
        );
      })
      .catch((error) => {
        console.log(error);
      })
      .finally((_) => {
        setIsLoading((prev) => prev - 1);
      });
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
      ppVerbs[ppId] = { ...ppVerbs[ppId], [name]: value.toLowerCase() };
      return { ...prev, ppVerbs };
    });
  };

  if (isLoading > 0 || infinitive === null) return <div>loading...</div>;
  return (
    <div className={cx("container")}>
      <form onSubmit={submitHandler}>
        <div className={cx("card")}>
          <div className={cx("input-wrapper")}>
            <div className={cx("input-row")}>
              <label>Слово:</label>
              <input
                type="text"
                name="word"
                placeholder="Слово"
                value={infinitive.word}
                onChange={(e) =>
                  setInfinitive((prev) => ({ ...prev, word: e.target.value }))
                }
              />
            </div>
            <div className={cx("input-row")}>
              <label>Перевод:</label>
              <input
                type="text"
                name="translate"
                placeholder="Перевод"
                value={infinitive.translate}
                onChange={(e) =>
                  setInfinitive((prev) => ({
                    ...prev,
                    translate: e.target.value,
                  }))
                }
              />
            </div>
          </div>
        </div>
        <div className={cx("card")}>
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
                    onChange={(e) =>
                      uodatePPVerb(e.target, personal_pronoun.id)
                    }
                  />
                </div>
                <div className={cx("input-row")}>
                  <label>{personal_pronoun.translate}</label>
                  <input
                    type="text"
                    name="translate"
                    placeholder="translate"
                    value={verb.translate}
                    onChange={(e) =>
                      uodatePPVerb(e.target, personal_pronoun.id)
                    }
                  />
                </div>
              </div>
            );
          })}
        </div>
        <div className={cx("send-button")}>
          <button>сохранить</button>
        </div>
      </form>
    </div>
  );
}

export default UpdateWord;
