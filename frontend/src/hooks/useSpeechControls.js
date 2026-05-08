import { useEffect, useRef, useState } from "react";

export function useSpeechControls() {
  const utteranceRef = useRef(null);
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [speed, setSpeed] = useState(1);

  useEffect(() => () => window.speechSynthesis.cancel(), []);

  const speak = (text) => {
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.rate = speed;
    utterance.onend = () => setIsSpeaking(false);
    utteranceRef.current = utterance;
    setIsSpeaking(true);
    window.speechSynthesis.speak(utterance);
  };

  return {
    isSpeaking,
    speed,
    setSpeed,
    speak,
    pause: () => window.speechSynthesis.pause(),
    resume: () => window.speechSynthesis.resume(),
    stop: () => {
      window.speechSynthesis.cancel();
      setIsSpeaking(false);
    },
  };
}

