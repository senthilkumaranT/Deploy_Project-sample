import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { MessageCircle, Sparkles, Zap, ArrowRight } from "lucide-react";

interface LandingPageProps {
  onEnterChat: () => void;
}

const LandingPage = ({ onEnterChat }: LandingPageProps) => {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center p-6 relative overflow-hidden">
      {/* Background decoration */}
      <div className="absolute inset-0 bg-gradient-to-br from-primary/10 via-transparent to-primary-glow/10" />
      
      <div className="container mx-auto max-w-4xl relative z-10">
        {/* Hero Section */}
        <div className="text-center mb-16 animate-fade-in">
          <div className="flex justify-center mb-6">
            <div className="p-4 rounded-full bg-gradient-to-r from-primary to-primary-glow glow-effect">
              <MessageCircle className="w-12 h-12 text-primary-foreground" />
            </div>
          </div>
          
          <h1 className="text-6xl font-bold mb-6 hero-text leading-tight">
            AI Q&A Chatbot
          </h1>
          
          <p className="text-xl text-muted-foreground mb-8 max-w-2xl mx-auto">
            Get instant answers to your questions with our intelligent chatbot. 
            Powered by advanced AI technology for accurate and helpful responses.
          </p>
          
          <Button 
            onClick={onEnterChat}
            size="lg"
            className="bg-gradient-to-r from-primary to-primary-glow hover:from-primary-glow hover:to-primary text-primary-foreground px-8 py-6 text-lg rounded-full transition-all duration-300 hover:scale-105 glow-effect group"
          >
            Start Chatting
            <ArrowRight className="ml-2 w-5 h-5 group-hover:translate-x-1 transition-transform" />
          </Button>
        </div>

        {/* Features Grid */}
        <div className="grid md:grid-cols-3 gap-6 mb-16">
          <Card className="p-6 bg-card/50 backdrop-blur-sm border-border hover:border-primary/50 transition-all duration-300 animate-slide-up">
            <div className="flex items-center mb-4">
              <Sparkles className="w-8 h-8 text-primary mr-3" />
              <h3 className="text-xl font-semibold">Intelligent Responses</h3>
            </div>
            <p className="text-muted-foreground">
              Advanced AI algorithms provide accurate and contextual answers to your questions.
            </p>
          </Card>

          <Card className="p-6 bg-card/50 backdrop-blur-sm border-border hover:border-primary/50 transition-all duration-300 animate-slide-up" style={{animationDelay: '0.1s'}}>
            <div className="flex items-center mb-4">
              <Zap className="w-8 h-8 text-primary mr-3" />
              <h3 className="text-xl font-semibold">Lightning Fast</h3>
            </div>
            <p className="text-muted-foreground">
              Get instant responses without any delays. Our chatbot is optimized for speed.
            </p>
          </Card>

          <Card className="p-6 bg-card/50 backdrop-blur-sm border-border hover:border-primary/50 transition-all duration-300 animate-slide-up" style={{animationDelay: '0.2s'}}>
            <div className="flex items-center mb-4">
              <MessageCircle className="w-8 h-8 text-primary mr-3" />
              <h3 className="text-xl font-semibold">Natural Conversation</h3>
            </div>
            <p className="text-muted-foreground">
              Experience human-like conversations with our advanced natural language processing.
            </p>
          </Card>
        </div>

        {/* Call to Action */}
        <div className="text-center animate-fade-in">
          <p className="text-muted-foreground mb-4">
            Ready to experience the future of Q&A?
          </p>
          <Button 
            onClick={onEnterChat}
            variant="outline"
            className="border-primary text-primary hover:bg-primary hover:text-primary-foreground transition-all duration-300"
          >
            Enter Chatbot
          </Button>
        </div>
      </div>
    </div>
  );
};

export default LandingPage;