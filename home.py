import React, { useState, useEffect } from 'react';
import { Search, Plus, Heart, Share2, Download, Menu, X, Home, Bell, MessageCircle, User, Upload, Image as ImageIcon, Send, ChevronLeft } from 'lucide-react';

const ASHNImages = () => {
  const [currentUser, setCurrentUser] = useState(null);
  const [showAuth, setShowAuth] = useState(false);
  const [authMode, setAuthMode] = useState('login');
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedImage, setSelectedImage] = useState(null);
  const [showUpload, setShowUpload] = useState(false);
  const [showNotifications, setShowNotifications] = useState(false);
  const [showMessages, setShowMessages] = useState(false);
  const [selectedChat, setSelectedChat] = useState(null);
  const [messageText, setMessageText] = useState('');
  
  // États pour les données
  const [users, setUsers] = useState([
    { id: 1, username: 'demo', email: 'demo@ashn.com', password: 'demo123', name: 'Demo User', avatar: null, followers: 245, following: 189 },
    { id: 2, username: 'NaturePhoto', email: 'nature@ashn.com', password: 'pass123', name: 'Nature Photographer', avatar: null, followers: 1200, following: 450 },
    { id: 3, username: 'HomeDesign', email: 'home@ashn.com', password: 'pass123', name: 'Home Designer', avatar: null, followers: 890, following: 234 }
  ]);
  
  const [images, setImages] = useState([
    { id: 1, url: 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=400', title: 'Mountain Landscape', userId: 2, category: 'Nature', likes: 234, saves: 89, timestamp: new Date('2025-10-28') },
    { id: 2, url: 'https://images.unsplash.com/photo-1511884642898-4c92249e20b6?w=400', title: 'Modern Kitchen', userId: 3, category: 'Interior', likes: 156, saves: 67, timestamp: new Date('2025-10-29') },
    { id: 3, url: 'https://images.unsplash.com/photo-1490730141103-6cac27aaab94?w=400', title: 'Fashion Style', userId: 2, category: 'Fashion', likes: 445, saves: 123, timestamp: new Date('2025-10-30') },
    { id: 4, url: 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=400', title: 'Portrait', userId: 3, category: 'People', likes: 678, saves: 234, timestamp: new Date('2025-10-27') },
    { id: 5, url: 'https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=400', title: 'City Architecture', userId: 2, category: 'Architecture', likes: 321, saves: 145, timestamp: new Date('2025-10-26') },
    { id: 6, url: 'https://images.unsplash.com/photo-1493612276216-ee3925520721?w=400', title: 'Minimal Design', userId: 3, category: 'Design', likes: 567, saves: 189, timestamp: new Date('2025-10-31') },
  ]);

  const [savedImages, setSavedImages] = useState({});
  const [likedImages, setLikedImages] = useState({});
  
  const [notifications, setNotifications] = useState([
    { id: 1, type: 'like', user: 'NaturePhoto', message: 'a aimé votre photo', time: '5 min', read: false },
    { id: 2, type: 'follow', user: 'HomeDesign', message: "s'est abonné à vous", time: '1 h', read: false },
    { id: 3, type: 'comment', user: 'NaturePhoto', message: 'a commenté votre photo', time: '2 h', read: true },
    { id: 4, type: 'save', user: 'HomeDesign', message: 'a enregistré votre photo', time: '3 h', read: true },
  ]);

  const [conversations, setConversations] = useState([
    { 
      id: 1, 
      userId: 2, 
      username: 'NaturePhoto', 
      lastMessage: 'Super photo ! Tu utilises quel appareil ?',
      time: '10 min',
      unread: 2,
      messages: [
        { id: 1, senderId: 2, text: 'Salut ! Magnifique photo', time: '2 h', isOwn: false },
        { id: 2, senderId: 1, text: 'Merci beaucoup !', time: '1 h 50', isOwn: true },
        { id: 3, senderId: 2, text: 'Super photo ! Tu utilises quel appareil ?', time: '10 min', isOwn: false }
      ]
    },
    { 
      id: 2, 
      userId: 3, 
      username: 'HomeDesign', 
      lastMessage: "J'adore ton style !",
      time: '1 h',
      unread: 0,
      messages: [
        { id: 1, senderId: 3, text: "J'adore ton style !", time: '1 h', isOwn: false }
      ]
    }
  ]);

  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    name: ''
  });

  const [uploadData, setUploadData] = useState({
    title: '',
    category: '',
    imageUrl: ''
  });

  // Formulaire d'authentification
  const AuthModal = () => (
    <div className="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center p-4">
      <div className="bg-white rounded-3xl max-w-md w-full p-8">
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-2xl font-bold">
            {authMode === 'login' ? 'Connexion' : 'Inscription'}
          </h2>
          <button onClick={() => setShowAuth(false)} className="p-2 hover:bg-gray-100 rounded-full">
            <X className="w-5 h-5" />
          </button>
        </div>

        <form onSubmit={handleAuth} className="space-y-4">
          {authMode === 'signup' && (
            <>
              <input
                type="text"
                placeholder="Nom complet"
                value={formData.name}
                onChange={(e) => setFormData({...formData, name: e.target.value})}
                className="w-full px-4 py-3 border rounded-full focus:outline-none focus:border-red-600"
                required
              />
              <input
                type="text"
                placeholder="Nom d'utilisateur"
                value={formData.username}
                onChange={(e) => setFormData({...formData, username: e.target.value})}
                className="w-full px-4 py-3 border rounded-full focus:outline-none focus:border-red-600"
                required
              />
            </>
          )}
          <input
            type="email"
            placeholder="Email"
            value={formData.email}
            onChange={(e) => setFormData({...formData, email: e.target.value})}
            className="w-full px-4 py-3 border rounded-full focus:outline-none focus:border-red-600"
            required
          />
          <input
            type="password"
            placeholder="Mot de passe"
            value={formData.password}
            onChange={(e) => setFormData({...formData, password: e.target.value})}
            className="w-full px-4 py-3 border rounded-full focus:outline-none focus:border-red-600"
            required
          />
          <button
            type="submit"
            className="w-full py-3 bg-red-600 text-white rounded-full font-semibold hover:bg-red-700"
          >
            {authMode === 'login' ? 'Se connecter' : "S'inscrire"}
          </button>
        </form>

        <div className="mt-6 text-center">
          <button
            onClick={() => setAuthMode(authMode === 'login' ? 'signup' : 'login')}
            className="text-red-600 hover:underline"
          >
            {authMode === 'login' ? "Pas de compte ? S'inscrire" : 'Déjà un compte ? Se connecter'}
          </button>
        </div>

        {authMode === 'login' && (
          <div className="mt-4 p-4 bg-gray-100 rounded-lg text-sm">
            <p className="font-semibold mb-2">Compte de démonstration :</p>
            <p>Email : demo@ashn.com</p>
            <p>Mot de passe : demo123</p>
          </div>
        )}
      </div>
    </div>
  );

  // Modal de publication
  const UploadModal = () => (
    <div className="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center p-4">
      <div className="bg-white rounded-3xl max-w-2xl w-full p-8">
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-2xl font-bold">Publier une image</h2>
          <button onClick={() => setShowUpload(false)} className="p-2 hover:bg-gray-100 rounded-full">
            <X className="w-5 h-5" />
          </button>
        </div>

        <form onSubmit={handleUpload} className="space-y-4">
          <div className="border-2 border-dashed border-gray-300 rounded-2xl p-8 text-center">
            <Upload className="w-12 h-12 mx-auto mb-4 text-gray-400" />
            <input
              type="text"
              placeholder="URL de l'image"
              value={uploadData.imageUrl}
              onChange={(e) => setUploadData({...uploadData, imageUrl: e.target.value})}
              className="w-full px-4 py-2 border rounded-full focus:outline-none focus:border-red-600"
              required
            />
            {uploadData.imageUrl && (
              <img src={uploadData.imageUrl} alt="Preview" className="mt-4 max-h-40 mx-auto rounded-lg" />
            )}
          </div>

          <input
            type="text"
            placeholder="Titre de l'image"
            value={uploadData.title}
            onChange={(e) => setUploadData({...uploadData, title: e.target.value})}
            className="w-full px-4 py-3 border rounded-full focus:outline-none focus:border-red-600"
            required
          />

          <select
            value={uploadData.category}
            onChange={(e) => setUploadData({...uploadData, category: e.target.value})}
            className="w-full px-4 py-3 border rounded-full focus:outline-none focus:border-red-600"
            required
          >
            <option value="">Sélectionner une catégorie</option>
            <option value="Nature">Nature</option>
            <option value="Design">Design</option>
            <option value="Fashion">Mode</option>
            <option value="Interior">Intérieur</option>
            <option value="Architecture">Architecture</option>
            <option value="Food">Cuisine</option>
            <option value="Travel">Voyage</option>
          </select>

          <button
            type="submit"
            className="w-full py-3 bg-red-600 text-white rounded-full font-semibold hover:bg-red-700"
          >
            Publier
          </button>
        </form>
      </div>
    </div>
  );

  // Panel de notifications
  const NotificationPanel = () => (
    <div className="fixed top-16 right-4 w-96 bg-white rounded-2xl shadow-2xl z-50 max-h-[600px] overflow-hidden">
      <div className="p-4 border-b">
        <div className="flex items-center justify-between">
          <h3 className="font-bold text-lg">Notifications</h3>
          <button onClick={() => setShowNotifications(false)} className="p-1 hover:bg-gray-100 rounded-full">
            <X className="w-5 h-5" />
          </button>
        </div>
      </div>
      <div className="overflow-y-auto max-h-[540px]">
        {notifications.map(notif => (
          <div key={notif.id} className={`p-4 hover:bg-gray-50 cursor-pointer border-b ${!notif.read ? 'bg-red-50' : ''}`}>
            <div className="flex gap-3">
              <div className="w-10 h-10 bg-gray-300 rounded-full flex-shrink-0"></div>
              <div className="flex-1">
                <p className="text-sm">
                  <span className="font-semibold">{notif.user}</span> {notif.message}
                </p>
                <p className="text-xs text-gray-500 mt-1">{notif.time}</p>
              </div>
              {!notif.read && <div className="w-2 h-2 bg-red-600 rounded-full"></div>}
            </div>
          </div>
        ))}
      </div>
    </div>
  );

  // Panel de messages
  const MessagesPanel = () => (
    <div className="fixed top-16 right-4 w-96 bg-white rounded-2xl shadow-2xl z-50 max-h-[600px] overflow-hidden flex flex-col">
      {!selectedChat ? (
        <>
          <div className="p-4 border-b">
            <div className="flex items-center justify-between">
              <h3 className="font-bold text-lg">Messages</h3>
              <button onClick={() => setShowMessages(false)} className="p-1 hover:bg-gray-100 rounded-full">
                <X className="w-5 h-5" />
              </button>
            </div>
          </div>
          <div className="overflow-y-auto flex-1">
            {conversations.map(conv => (
              <div 
                key={conv.id} 
                onClick={() => setSelectedChat(conv)}
                className="p-4 hover:bg-gray-50 cursor-pointer border-b"
              >
                <div className="mb-6">
                  <span className="inline-block px-4 py-2 bg-gray-100 rounded-full text-sm font-medium">
                    {selectedImage.category}
                  </span>
                </div>
                <div className="flex items-center gap-6 mb-6 text-sm text-gray-600">
                  <div className="flex items-center gap-2">
                    <Heart className="w-4 h-4" />
                    <span>{selectedImage.likes} j'aime</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <Download className="w-4 h-4" />
                    <span>{selectedImage.saves} enregistrements</span>
                  </div>
                </div>
                <div className="border-t pt-6">
                  <h3 className="font-semibold mb-4">Commentaires</h3>
                  {currentUser ? (
                    <div className="flex gap-3">
                      <div className="w-10 h-10 bg-gradient-to-br from-red-400 to-red-600 rounded-full flex items-center justify-center text-white font-bold flex-shrink-0">
                        {currentUser.name.charAt(0)}
                      </div>
                      <input
                        type="text"
                        placeholder="Ajouter un commentaire"
                        className="flex-1 px-4 py-2 border rounded-full focus:outline-none focus:border-gray-400"
                      />
                    </div>
                  ) : (
                    <button 
                      onClick={() => setShowAuth(true)}
                      className="text-red-600 hover:underline"
                    >
                      Connectez-vous pour commenter
                    </button>
                  )}
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

      {currentUser && (
        <button 
          onClick={() => setShowUpload(true)}
          className="fixed bottom-8 right-8 w-14 h-14 bg-red-600 hover:bg-red-700 text-white rounded-full shadow-lg flex items-center justify-center z-40"
        >
          <Plus className="w-6 h-6" />
        </button>
      )}

      {showAuth && <AuthModal />}
      {showUpload && <UploadModal />}
      {showNotifications && <NotificationPanel />}
      {showMessages && <MessagesPanel />}
    </div>
  );
};

export default ASHNImages; className="flex gap-3">
                  <div className="w-12 h-12 bg-gray-300 rounded-full flex-shrink-0"></div>
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center justify-between mb-1">
                      <p className="font-semibold truncate">{conv.username}</p>
                      <span className="text-xs text-gray-500">{conv.time}</span>
                    </div>
                    <p className="text-sm text-gray-600 truncate">{conv.lastMessage}</p>
                  </div>
                  {conv.unread > 0 && (
                    <div className="w-5 h-5 bg-red-600 rounded-full flex items-center justify-center text-white text-xs">
                      {conv.unread}
                    </div>
                  )}
                </div>
              </div>
            ))}
          </div>
        </>
      ) : (
        <>
          <div className="p-4 border-b flex items-center gap-3">
            <button onClick={() => setSelectedChat(null)} className="p-1 hover:bg-gray-100 rounded-full">
              <ChevronLeft className="w-5 h-5" />
            </button>
            <div className="w-10 h-10 bg-gray-300 rounded-full"></div>
            <h3 className="font-bold flex-1">{selectedChat.username}</h3>
            <button onClick={() => setShowMessages(false)} className="p-1 hover:bg-gray-100 rounded-full">
              <X className="w-5 h-5" />
            </button>
          </div>
          <div className="flex-1 overflow-y-auto p-4 space-y-3">
            {selectedChat.messages.map(msg => (
              <div key={msg.id} className={`flex ${msg.isOwn ? 'justify-end' : 'justify-start'}`}>
                <div className={`max-w-[70%] px-4 py-2 rounded-2xl ${msg.isOwn ? 'bg-red-600 text-white' : 'bg-gray-200'}`}>
                  <p className="text-sm">{msg.text}</p>
                  <p className={`text-xs mt-1 ${msg.isOwn ? 'text-red-100' : 'text-gray-500'}`}>{msg.time}</p>
                </div>
              </div>
            ))}
          </div>
          <div className="p-4 border-t">
            <form onSubmit={handleSendMessage} className="flex gap-2">
              <input
                type="text"
                value={messageText}
                onChange={(e) => setMessageText(e.target.value)}
                placeholder="Écrire un message..."
                className="flex-1 px-4 py-2 border rounded-full focus:outline-none focus:border-red-600"
              />
              <button type="submit" className="p-2 bg-red-600 text-white rounded-full hover:bg-red-700">
                <Send className="w-5 h-5" />
              </button>
            </form>
          </div>
        </>
      )}
    </div>
  );

  const handleAuth = (e) => {
    e.preventDefault();
    if (authMode === 'login') {
      const user = users.find(u => u.email === formData.email && u.password === formData.password);
      if (user) {
        setCurrentUser(user);
        setShowAuth(false);
        setFormData({ username: '', email: '', password: '', name: '' });
      } else {
        alert('Email ou mot de passe incorrect');
      }
    } else {
      const newUser = {
        id: users.length + 1,
        ...formData,
        avatar: null,
        followers: 0,
        following: 0
      };
      setUsers([...users, newUser]);
      setCurrentUser(newUser);
      setShowAuth(false);
      setFormData({ username: '', email: '', password: '', name: '' });
    }
  };

  const handleUpload = (e) => {
    e.preventDefault();
    if (!currentUser) return;
    
    const newImage = {
      id: images.length + 1,
      ...uploadData,
      userId: currentUser.id,
      likes: 0,
      saves: 0,
      timestamp: new Date()
    };
    setImages([newImage, ...images]);
    setShowUpload(false);
    setUploadData({ title: '', category: '', imageUrl: '' });
  };

  const handleSendMessage = (e) => {
    e.preventDefault();
    if (!messageText.trim()) return;
    
    const newMessage = {
      id: selectedChat.messages.length + 1,
      senderId: currentUser.id,
      text: messageText,
      time: 'À l\'instant',
      isOwn: true
    };
    
    setConversations(conversations.map(conv => 
      conv.id === selectedChat.id 
        ? { ...conv, messages: [...conv.messages, newMessage], lastMessage: messageText, time: 'À l\'instant' }
        : conv
    ));
    
    setSelectedChat({
      ...selectedChat,
      messages: [...selectedChat.messages, newMessage]
    });
    
    setMessageText('');
  };

  const handleSave = (imageId) => {
    setSavedImages(prev => ({
      ...prev,
      [imageId]: !prev[imageId]
    }));
  };

  const handleLike = (imageId) => {
    setLikedImages(prev => ({
      ...prev,
      [imageId]: !prev[imageId]
    }));
  };

  const getUserById = (userId) => users.find(u => u.id === userId);

  const filteredImages = searchQuery
    ? images.filter(img => 
        img.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
        img.category.toLowerCase().includes(searchQuery.toLowerCase())
      )
    : images;

  const unreadNotifications = notifications.filter(n => !n.read).length;
  const unreadMessages = conversations.reduce((sum, conv) => sum + conv.unread, 0);

  return (
    <div className="min-h-screen bg-white">
      {/* Header */}
      <header className="fixed top-0 left-0 right-0 bg-white shadow-sm z-40">
        <div className="max-w-screen-2xl mx-auto px-4 py-3 flex items-center gap-4">
          <div className="flex items-center gap-2">
            <div className="w-10 h-10 bg-red-600 rounded-full flex items-center justify-center text-white font-bold text-xl">
              A
            </div>
            <span className="font-bold text-xl hidden sm:block">ASHN Images</span>
          </div>

          <nav className="hidden md:flex gap-4">
            <button className="px-4 py-2 rounded-full hover:bg-gray-100 font-semibold">Accueil</button>
            <button className="px-4 py-2 rounded-full hover:bg-gray-100">Aujourd'hui</button>
          </nav>

          <div className="flex-1 max-w-3xl">
            <div className="relative">
              <Search className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400 w-5 h-5" />
              <input
                type="text"
                placeholder="Rechercher"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full pl-12 pr-4 py-3 bg-gray-100 rounded-full focus:outline-none focus:bg-gray-200"
              />
            </div>
          </div>

          <div className="flex items-center gap-2">
            {currentUser ? (
              <>
                <div className="relative">
                  <button 
                    onClick={() => {
                      setShowNotifications(!showNotifications);
                      setShowMessages(false);
                    }}
                    className="p-2 hover:bg-gray-100 rounded-full relative"
                  >
                    <Bell className="w-6 h-6" />
                    {unreadNotifications > 0 && (
                      <span className="absolute top-1 right-1 w-4 h-4 bg-red-600 text-white text-xs rounded-full flex items-center justify-center">
                        {unreadNotifications}
                      </span>
                    )}
                  </button>
                </div>
                <div className="relative">
                  <button 
                    onClick={() => {
                      setShowMessages(!showMessages);
                      setShowNotifications(false);
                    }}
                    className="p-2 hover:bg-gray-100 rounded-full relative"
                  >
                    <MessageCircle className="w-6 h-6" />
                    {unreadMessages > 0 && (
                      <span className="absolute top-1 right-1 w-4 h-4 bg-red-600 text-white text-xs rounded-full flex items-center justify-center">
                        {unreadMessages}
                      </span>
                    )}
                  </button>
                </div>
                <button className="w-10 h-10 bg-gradient-to-br from-red-400 to-red-600 rounded-full flex items-center justify-center text-white font-bold">
                  {currentUser.name.charAt(0)}
                </button>
                <button 
                  onClick={() => setCurrentUser(null)}
                  className="px-4 py-2 text-sm hover:bg-gray-100 rounded-full"
                >
                  Déconnexion
                </button>
              </>
            ) : (
              <button 
                onClick={() => setShowAuth(true)}
                className="px-6 py-2 bg-red-600 text-white rounded-full font-semibold hover:bg-red-700"
              >
                Connexion
              </button>
            )}
          </div>
        </div>
      </header>

      <main className="pt-20 px-4 max-w-screen-2xl mx-auto">
        <div className="flex gap-2 mb-6 overflow-x-auto pb-2">
          {['Tous', 'Design', 'Mode', 'Nature', 'Architecture', 'Cuisine', 'Voyage'].map((cat) => (
            <button key={cat} className="px-4 py-2 bg-gray-100 hover:bg-gray-200 rounded-full whitespace-nowrap font-medium">
              {cat}
            </button>
          ))}
        </div>

        <div className="columns-2 sm:columns-3 lg:columns-4 xl:columns-5 gap-4 space-y-4">
          {filteredImages.map((image) => {
            const imageUser = getUserById(image.userId);
            return (
              <div key={image.id} className="break-inside-avoid group relative cursor-pointer" onClick={() => setSelectedImage(image)}>
                <div className="relative overflow-hidden rounded-2xl">
                  <img src={image.url} alt={image.title} className="w-full h-auto object-cover transition-transform duration-300 group-hover:scale-105" />
                  <div className="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-40 transition-opacity duration-300">
                    <div className="absolute top-4 right-4 opacity-0 group-hover:opacity-100 transition-opacity">
                      <button
                        onClick={(e) => {
                          e.stopPropagation();
                          if (!currentUser) {
                            setShowAuth(true);
                          } else {
                            handleSave(image.id);
                          }
                        }}
                        className={`px-4 py-2 rounded-full font-semibold ${savedImages[image.id] ? 'bg-black text-white' : 'bg-red-600 text-white hover:bg-red-700'}`}
                      >
                        {savedImages[image.id] ? 'Enregistré' : 'Enregistrer'}
                      </button>
                    </div>
                  </div>
                </div>
                <div className="mt-2 px-1">
                  <p className="font-semibold text-sm">{image.title}</p>
                  <p className="text-gray-600 text-xs">{imageUser?.username}</p>
                </div>
              </div>
            );
          })}
        </div>
      </main>

      {selectedImage && (
        <div className="fixed inset-0 bg-black bg-opacity-80 z-50 flex items-center justify-center p-4" onClick={() => setSelectedImage(null)}>
          <div className="bg-white rounded-3xl max-w-5xl w-full max-h-[90vh] overflow-auto" onClick={(e) => e.stopPropagation()}>
            <div className="grid md:grid-cols-2 gap-0">
              <div className="relative">
                <button onClick={() => setSelectedImage(null)} className="absolute top-4 right-4 p-2 bg-white rounded-full shadow-lg hover:bg-gray-100 z-10">
                  <X className="w-5 h-5" />
                </button>
                <img src={selectedImage.url} alt={selectedImage.title} className="w-full h-full object-cover rounded-l-3xl" />
              </div>
              <div className="p-8">
                <div className="flex items-center justify-between mb-6">
                  <div className="flex gap-2">
                    <button 
                      onClick={() => handleLike(selectedImage.id)}
                      className="p-2 hover:bg-gray-100 rounded-full"
                    >
                      <Heart className={`w-5 h-5 ${likedImages[selectedImage.id] ? 'fill-red-600 text-red-600' : ''}`} />
                    </button>
                    <button className="p-2 hover:bg-gray-100 rounded-full">
                      <Share2 className="w-5 h-5" />
                    </button>
                  </div>
                  <button
                    onClick={() => {
                      if (!currentUser) {
                        setShowAuth(true);
                      } else {
                        handleSave(selectedImage.id);
                      }
                    }}
                    className={`px-6 py-3 rounded-full font-semibold ${savedImages[selectedImage.id] ? 'bg-black text-white' : 'bg-red-600 text-white hover:bg-red-700'}`}
                  >
                    {savedImages[selectedImage.id] ? 'Enregistré' : 'Enregistrer'}
                  </button>
                </div>
                <h2 className="text-3xl font-bold mb-4">{selectedImage.title}</h2>
                <div className="flex items-center gap-3 mb-6">
                  <div className="w-12 h-12 bg-gradient-to-br from-red-400 to-red-600 rounded-full flex items-center justify-center text-white font-bold">
                    {getUserById(selectedImage.userId)?.name.charAt(0)}
                  </div>
                  <div>
                    <p className="font-semibold">{getUserById(selectedImage.userId)?.username}</p>
                    <p className="text-sm text-gray-600">{getUserById(selectedImage.userId)?.followers} abonnés</p>
                  </div>
                </div>
                <div
