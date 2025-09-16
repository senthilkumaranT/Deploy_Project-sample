import { useState } from "react";
import LandingPage from "@/components/LandingPage";
import ChatInterface from "@/components/ChatInterface";

const Index = () => {
  const [currentView, setCurrentView] = useState<'landing' | 'chat'>('landing');

  const handleEnterChat = () => {
    setCurrentView('chat');
  };

  const handleBackToLanding = () => {
    setCurrentView('landing');
  };

  return (
    <>
      {currentView === 'landing' ? (
        <LandingPage onEnterChat={handleEnterChat} />
      ) : (
        <ChatInterface onBackToLanding={handleBackToLanding} />
      )}
    </>
  );
};

export default Index;
