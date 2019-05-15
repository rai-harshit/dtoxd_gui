// -*- C++ -*-
//
// generated by wxGlade 0.9.0pre on Tue Jul 10 20:55:06 2018
//
// Example for compiling a single file project under Linux using g++:
//  g++ MyApp.cpp $(wx-config --libs) $(wx-config --cxxflags) -o MyApp
//
// Example for compiling a multi file project under Linux using g++:
//  g++ main.cpp $(wx-config --libs) $(wx-config --cxxflags) -o MyApp Dialog1.cpp Frame1.cpp
//

#include "FontTest.h"

// begin wxGlade: ::extracode
// end wxGlade



MyFrame::MyFrame(wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style):
    wxFrame(parent, id, title, pos, size, wxDEFAULT_FRAME_STYLE)
{
    // begin wxGlade: MyFrame::MyFrame
    SetSize(wxSize(400, 300));
    text_ctrl_1 = new wxTextCtrl(this, wxID_ANY, wxT("Some Input"), wxDefaultPosition, wxDefaultSize, wxTE_READONLY);

    set_properties();
    do_layout();
    // end wxGlade
}


void MyFrame::set_properties()
{
    // begin wxGlade: MyFrame::set_properties
    SetTitle(wxT("frame"));
    text_ctrl_1->SetBackgroundColour(wxColour(0, 255, 127));
    text_ctrl_1->SetForegroundColour(wxColour(255, 0, 0));
    text_ctrl_1->SetFont(wxFont(16, wxFONTFAMILY_DEFAULT, wxFONTSTYLE_NORMAL, wxFONTWEIGHT_BOLD, 0, wxT("")));
    text_ctrl_1->SetFocus();
    // end wxGlade
}


void MyFrame::do_layout()
{
    // begin wxGlade: MyFrame::do_layout
    wxBoxSizer* sizer_1 = new wxBoxSizer(wxVERTICAL);
    sizer_1->Add(text_ctrl_1, 1, wxALL|wxEXPAND, 5);
    wxStaticText* label_1 = new wxStaticText(this, wxID_ANY, wxT("label_1"));
    sizer_1->Add(label_1, 0, 0, 0);
    wxStaticText* label_2 = new wxStaticText(this, wxID_ANY, wxT("label_2"));
    label_2->SetFont(wxFont(8, wxFONTFAMILY_DECORATIVE, wxFONTSTYLE_SLANT, wxFONTWEIGHT_LIGHT, 0, wxT("")));
    sizer_1->Add(label_2, 0, 0, 0);
    wxStaticText* label_3 = new wxStaticText(this, wxID_ANY, wxT("label_3"));
    label_3->SetFont(wxFont(8, wxFONTFAMILY_ROMAN, wxFONTSTYLE_ITALIC, wxFONTWEIGHT_BOLD, 0, wxT("")));
    sizer_1->Add(label_3, 0, 0, 0);
    wxStaticText* label_4 = new wxStaticText(this, wxID_ANY, wxT("label_4"));
    label_4->SetFont(wxFont(8, wxFONTFAMILY_SCRIPT, wxFONTSTYLE_NORMAL, wxFONTWEIGHT_NORMAL, 0, wxT("")));
    sizer_1->Add(label_4, 0, 0, 0);
    wxStaticText* label_5 = new wxStaticText(this, wxID_ANY, wxT("label_5"));
    label_5->SetFont(wxFont(10, wxFONTFAMILY_SWISS, wxFONTSTYLE_NORMAL, wxFONTWEIGHT_NORMAL, 0, wxT("")));
    sizer_1->Add(label_5, 0, 0, 0);
    wxStaticText* label_6 = new wxStaticText(this, wxID_ANY, wxT("label_6"));
    label_6->SetFont(wxFont(12, wxFONTFAMILY_MODERN, wxFONTSTYLE_NORMAL, wxFONTWEIGHT_NORMAL, 1, wxT("")));
    sizer_1->Add(label_6, 0, 0, 0);
    SetSizer(sizer_1);
    Layout();
    // end wxGlade
}


class MyApp: public wxApp {
public:
    bool OnInit();
};

IMPLEMENT_APP(MyApp)

bool MyApp::OnInit()
{
    wxInitAllImageHandlers();
    MyFrame* frame = new MyFrame(NULL, wxID_ANY, wxEmptyString);
    SetTopWindow(frame);
    frame->Show();
    return true;
}
