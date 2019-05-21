#!/usr/bin/env python
# -*- coding: CP1252 -*-
#
# generated by wxGlade 0.9.3 on Mon May 20 18:04:51 2019
#

import wx
import wx.adv
import webbrowser

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class root_frame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: root_frame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.BORDER_SIMPLE | wx.CAPTION | wx.CLIP_CHILDREN | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.STAY_ON_TOP | wx.SYSTEM_MENU
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((720, 420))
        
        # Menu Bar
        self.frame_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        item = wxglade_tmp_menu.Append(wx.ID_ANY, "Quit", "Quit the application")
        self.Bind(wx.EVT_MENU, self.quit, id=item.GetId())
        self.frame_menubar.Append(wxglade_tmp_menu, "File")
        wxglade_tmp_menu = wx.Menu()
        item = wxglade_tmp_menu.Append(wx.ID_ANY, "Help", "Try documentation and tutorials")
        self.Bind(wx.EVT_MENU, self.documentation_help, id=item.GetId())
        item = wxglade_tmp_menu.Append(wx.ID_ANY, "Report Bugs", "Report bugs to Team dtoxd ")
        self.Bind(wx.EVT_MENU, self.report_bugs, id=item.GetId())
        item = wxglade_tmp_menu.Append(wx.ID_ANY, "Check for Updates", "Check for Updates")
        self.Bind(wx.EVT_MENU, self.check_for_updates, id=item.GetId())
        item = wxglade_tmp_menu.Append(wx.ID_ANY, "About dtoxd", "Learn more about dtoxd")
        self.Bind(wx.EVT_MENU, self.about_dtoxd, id=item.GetId())
        self.frame_menubar.Append(wxglade_tmp_menu, "About")
        self.SetMenuBar(self.frame_menubar)
        # Menu Bar end
        self.radio_btn_4 = wx.RadioButton(self, wx.ID_ANY, "", style=wx.RB_GROUP)
        self.radio_btn_5 = wx.RadioButton(self, wx.ID_ANY, "")
        self.radio_btn_1 = wx.RadioButton(self, wx.ID_ANY, "", style=wx.RB_GROUP)
        self.checkbox_3 = wx.CheckBox(self, wx.ID_ANY, "")
        self.checkbox_4 = wx.CheckBox(self, wx.ID_ANY, "")
        self.spin_ctrl_1 = wx.SpinCtrl(self, wx.ID_ANY, "1", min=0, max=23, style=wx.SP_WRAP)
        self.spin_ctrl_7 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=59, style=wx.SP_WRAP)
        self.choice_4 = wx.Choice(self, wx.ID_ANY, choices=["AM", "PM"])
        self.button_4 = wx.ToggleButton(self, wx.ID_ANY, "Scan Now")
        self.progressbar = wx.Gauge(self, wx.ID_ANY, 100)
        self.radio_btn_2 = wx.RadioButton(self, wx.ID_ANY, "")
        self.choice_2 = wx.Choice(self, wx.ID_ANY, choices=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
        self.spin_ctrl_3 = wx.SpinCtrl(self, wx.ID_ANY, "1", min=1, max=12, style=wx.SP_WRAP)
        self.spin_ctrl_4 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=59, style=wx.SP_WRAP)
        self.choice_5 = wx.Choice(self, wx.ID_ANY, choices=["AM", "PM"])
        self.checkbox_5 = wx.CheckBox(self, wx.ID_ANY, "")
        self.radio_btn_3 = wx.RadioButton(self, wx.ID_ANY, "")
        self.checkbox_6 = wx.CheckBox(self, wx.ID_ANY, "")
        self.choice_3 = wx.Choice(self, wx.ID_ANY, choices=["First Day", "Fortnightly", "Last Day"])
        self.spin_ctrl_5 = wx.SpinCtrl(self, wx.ID_ANY, "1", min=1, max=12, style=wx.SP_WRAP)
        self.spin_ctrl_6 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=59, style=wx.SP_WRAP)
        self.choice_6 = wx.Choice(self, wx.ID_ANY, choices=["AM", "PM"])
        self.button_5 = wx.Button(self, wx.ID_ANY, "Enable Real-time Moderation")
        self.hyperlink_1 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, "Got a feedback for us ?", "https://www.dtoxd.ai")
        self.button_3 = wx.Button(self, wx.ID_ANY, "OK")
        self.button_2 = wx.Button(self, wx.ID_ANY, "Cancel")
        self.button_1 = wx.Button(self, wx.ID_ANY, "Apply")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_RADIOBUTTON, self.scan_daily_schedule, self.radio_btn_1)
        self.Bind(wx.EVT_TOGGLEBUTTON, self.scan_toggle, self.button_4)
        self.Bind(wx.EVT_RADIOBUTTON, self.scan_weekly_schedule, self.radio_btn_2)
        self.Bind(wx.EVT_CHECKBOX, self.realtime_processing, self.checkbox_5)
        self.Bind(wx.EVT_RADIOBUTTON, self.scan_monthly_schedule, self.radio_btn_3)
        self.Bind(wx.EVT_CHECKBOX, self.realtime_processing, self.checkbox_6)
        self.Bind(wx.EVT_BUTTON, self.apply_and_close, self.button_3)
        self.Bind(wx.EVT_BUTTON, self.quit, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.apply_settings, self.button_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: root_frame.__set_properties
        self.SetTitle("dtoxd : The Clean Digital Experience")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("src\\dtoxd_logo_24x24.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.SetFocus()
        self.radio_btn_4.SetValue(1)
        self.radio_btn_1.SetFocus()
        self.radio_btn_1.SetValue(1)
        self.spin_ctrl_1.SetMinSize((42, 20))
        self.spin_ctrl_7.SetMinSize((42, 20))
        self.choice_4.SetMinSize((44, 22))
        self.choice_4.SetSelection(0)
        self.progressbar.SetMinSize((175, 25))
        self.progressbar.Hide()
        self.choice_2.Enable(False)
        self.choice_2.SetSelection(0)
        self.spin_ctrl_3.SetMinSize((40, 20))
        self.spin_ctrl_3.Enable(False)
        self.spin_ctrl_4.SetMinSize((42, 20))
        self.spin_ctrl_4.Enable(False)
        self.choice_5.SetMinSize((44, 22))
        self.choice_5.Enable(False)
        self.choice_5.SetSelection(0)
        self.checkbox_5.Enable(False)
        self.checkbox_6.Enable(False)
        self.choice_3.Enable(False)
        self.choice_3.SetSelection(0)
        self.spin_ctrl_5.SetMinSize((40, 20))
        self.spin_ctrl_5.Enable(False)
        self.spin_ctrl_6.SetMinSize((42, 20))
        self.spin_ctrl_6.Enable(False)
        self.choice_6.SetMinSize((44, 22))
        self.choice_6.Enable(False)
        self.choice_6.SetSelection(0)
        self.button_5.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.button_5.Enable(False)
        self.hyperlink_1.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Calibri"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: root_frame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(9, 13, 0, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, "Content Scanner")
        label_3.SetForegroundColour(wx.Colour(0, 0, 0))
        label_3.SetFont(wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Calibri"))
        grid_sizer_1.Add(label_3, 0, wx.LEFT | wx.TOP, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        static_line_1 = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_VERTICAL)
        static_line_1.SetMinSize((4, 400))
        grid_sizer_1.Add(static_line_1, 0, wx.LEFT, 10)
        label_1 = wx.StaticText(self, wx.ID_ANY, "Schedule Scan")
        label_1.SetForegroundColour(wx.Colour(0, 0, 0))
        label_1.SetFont(wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Calibri"))
        grid_sizer_1.Add(label_1, 0, wx.TOP, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.radio_btn_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.TOP, 20)
        label_2 = wx.StaticText(self, wx.ID_ANY, "Quick Scan")
        grid_sizer_1.Add(label_2, 0, wx.LEFT | wx.TOP, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.radio_btn_5, 0, wx.LEFT | wx.TOP, 20)
        label_9 = wx.StaticText(self, wx.ID_ANY, "Deep Scan")
        grid_sizer_1.Add(label_9, 0, wx.LEFT | wx.TOP, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.radio_btn_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 0)
        label_10 = wx.StaticText(self, wx.ID_ANY, "Daily")
        label_10.SetForegroundColour(wx.Colour(0, 0, 0))
        label_10.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Calibri"))
        grid_sizer_1.Add(label_10, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.checkbox_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 19)
        label_4 = wx.StaticText(self, wx.ID_ANY, "Images")
        label_4.SetForegroundColour(wx.Colour(0, 0, 0))
        label_4.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Calibri"))
        grid_sizer_1.Add(label_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.checkbox_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        label_5 = wx.StaticText(self, wx.ID_ANY, "Videos")
        label_5.SetForegroundColour(wx.Colour(0, 0, 0))
        label_5.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Calibri"))
        grid_sizer_1.Add(label_5, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.spin_ctrl_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 55)
        label_15 = wx.StaticText(self, wx.ID_ANY, ":")
        label_15.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        grid_sizer_1.Add(label_15, 0, wx.ALIGN_CENTER | wx.LEFT, 50)
        grid_sizer_1.Add(self.spin_ctrl_7, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 5)
        grid_sizer_1.Add(self.choice_4, 0, wx.ALIGN_CENTER | wx.LEFT, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.button_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 18)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.progressbar, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 10)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.radio_btn_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 0)
        label_11 = wx.StaticText(self, wx.ID_ANY, "Weekly")
        label_11.SetForegroundColour(wx.Colour(0, 0, 0))
        label_11.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Calibri"))
        grid_sizer_1.Add(label_11, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        label_6 = wx.StaticText(self, wx.ID_ANY, "Real-time Content Moderation")
        label_6.SetForegroundColour(wx.Colour(0, 0, 0))
        label_6.SetFont(wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Calibri"))
        grid_sizer_1.Add(label_6, 0, wx.LEFT | wx.TOP, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.choice_2, 0, wx.ALIGN_CENTER | wx.LEFT, 30)
        grid_sizer_1.Add(self.spin_ctrl_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 50)
        label_14 = wx.StaticText(self, wx.ID_ANY, ":")
        label_14.SetForegroundColour(wx.Colour(0, 0, 0))
        grid_sizer_1.Add(label_14, 0, wx.ALIGN_CENTER | wx.LEFT, 35)
        grid_sizer_1.Add(self.spin_ctrl_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 10)
        grid_sizer_1.Add(self.choice_5, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 10)
        grid_sizer_1.Add(self.checkbox_5, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        label_7 = wx.StaticText(self, wx.ID_ANY, "Images")
        label_7.SetForegroundColour(wx.Colour(0, 0, 0))
        label_7.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Calibri"))
        grid_sizer_1.Add(label_7, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.radio_btn_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 0)
        label_12 = wx.StaticText(self, wx.ID_ANY, "Monthly")
        label_12.SetForegroundColour(wx.Colour(0, 0, 0))
        label_12.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Calibri"))
        grid_sizer_1.Add(label_12, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.checkbox_6, 0, wx.LEFT, 20)
        label_8 = wx.StaticText(self, wx.ID_ANY, "Videos")
        label_8.SetForegroundColour(wx.Colour(0, 0, 0))
        label_8.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Calibri"))
        grid_sizer_1.Add(label_8, 0, wx.LEFT, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.choice_3, 0, wx.ALIGN_CENTER | wx.LEFT, 30)
        grid_sizer_1.Add(self.spin_ctrl_5, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 50)
        label_16 = wx.StaticText(self, wx.ID_ANY, ":")
        label_16.SetForegroundColour(wx.Colour(0, 0, 0))
        grid_sizer_1.Add(label_16, 0, wx.ALIGN_CENTER | wx.LEFT, 35)
        grid_sizer_1.Add(self.spin_ctrl_6, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 10)
        grid_sizer_1.Add(self.choice_6, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 10)
        grid_sizer_1.Add(self.button_5, 0, wx.LEFT, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.hyperlink_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.LEFT, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.button_3, 0, wx.ALIGN_RIGHT | wx.RIGHT, 10)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.button_2, 0, wx.ALIGN_RIGHT | wx.RIGHT, 10)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.button_1, 0, wx.ALIGN_RIGHT | wx.RIGHT, 10)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.Centre()
        # end wxGlade

    def quit(self, event):  # wxGlade: root_frame.<event_handler>
        # print("Event handler 'quit' not implemented!")
        # event.Skip()
        self.Close()

    def documentation_help(self, event):  # wxGlade: root_frame.<event_handler>
        # print("Event handler 'documentation_help' not implemented!")
        # event.Skip()
        webbrowser.open_new_tab("https://www.dtoxd.ai")

    def report_bugs(self, event):  # wxGlade: root_frame.<event_handler>
        # print("Event handler 'report_bugs' not implemented!")
        # event.Skip()
        webbrowser.open_new_tab("https://www.dtoxd.ai")

    def check_for_updates(self, event):  # wxGlade: root_frame.<event_handler>
        # print("Event handler 'check_for_updates' not implemented!")
        # event.Skip()
        webbrowser.open_new_tab("https://www.dtoxd.ai")

    def about_dtoxd(self, event):  # wxGlade: root_frame.<event_handler>
        # print("Event handler 'about_dtoxd' not implemented!")
        # event.Skip()
        webbrowser.open_new_tab("https://www.dtoxd.ai")

    def scan_toggle(self, event):  # wxGlade: root_frame.<event_handler>
        # print("Event handler 'scan_toggle' not implemented!")
        # event.Skip()       
        scan_request = self.button_4.GetValue()
        cs_images_chkbox = self.checkbox_3.GetValue()
        cs_videos_chkbox = self.checkbox_4.GetValue()
        cs_scan_type = self.radio_btn_4.GetValue() 
        # Getting data from Scan Now options
        if scan_request is True:
            if cs_images_chkbox is True or cs_videos_chkbox is True:
                if cs_scan_type is True:
                    print("Quick Scan Mode Selected")
                else:
                    print("Deep Scan Mode Selected")
                print("Scan Started")
                self.progressbar.Pulse()
                #Disabling all the Radio Buttons and Checkboxes from Content Scanner
                self.radio_btn_4.Disable()
                self.radio_btn_5.Disable()
                self.checkbox_3.Disable()
                self.checkbox_4.Disable()
                self.button_4.SetLabel("Cancel")
                self.progressbar.Show()
            else:
                self.button_4.SetValue(False)
                wx.MessageBox("Select 'Images' or 'Videos' or both options to begin the scan.", "Attention !" ,wx.OK | wx.ICON_INFORMATION)
        if scan_request is False:
            print("Scan Stopped")
            self.progressbar.SetValue(0)
            self.radio_btn_4.Enable()
            self.radio_btn_5.Enable()
            self.checkbox_3.Enable()
            self.checkbox_4.Enable()
            self.progressbar.Hide()
            self.button_4.SetLabel("Scan Now")


        # cs_scan_type = self.radio_btn_4.GetValue()
        # print(cs_scan_type)
        # print(cs_images_chkbox)
        # print(cs_videos_chkbox)
        # if cs_scan_type == True:
        # 	print("Quick Scan Selected.")
        # else:
        # 	print("Deep Scan Selected.")
        # if cs_images_chkbox == False and cs_videos_chkbox == False:
        # 	wx.MessageBox("Select one or more options to continue.", "Attention !" ,wx.OK | wx.ICON_INFORMATION)
        # else:
        #     self.button_4.Hide()

    def scan_daily_schedule(self, event):  # wxGlade: root_frame.<event_handler>
        # print("Event handler 'scan_daily_schedule' not implemented!")
        # event.Skip()

        # Enable Daily Scan Controls
        self.spin_ctrl_1.Enable(True)
        self.spin_ctrl_7.Enable(True)
        self.choice_4.Enable(True)

        # Disable Weeklt Scan Controls
        self.choice_2.Enable(False)
        self.spin_ctrl_3.Enable(False)
        self.spin_ctrl_4.Enable(False)
        self.choice_5.Enable(False)

        # Disable Monthly Scan Controls
        self.choice_3.Enable(False)
        self.spin_ctrl_5.Enable(False)
        self.spin_ctrl_6.Enable(False)
        self.choice_6.Enable(False)

    def scan_weekly_schedule(self, event):  # wxGlade: root_frame.<event_handler>
        # print("Event handler 'scan_weekly_schedule' not implemented!")
        # event.Skip()

        # Disable Daily Scan Controls
        self.spin_ctrl_1.Enable(False)
        self.spin_ctrl_7.Enable(False)
        self.choice_4.Enable(False)

        # Enable Weeklt Scan Controls
        self.choice_2.Enable(True)
        self.spin_ctrl_3.Enable(True)
        self.spin_ctrl_4.Enable(True)
        self.choice_5.Enable(True)

        # Disable Monthly Scan Controls
        self.choice_3.Enable(False)
        self.spin_ctrl_5.Enable(False)
        self.spin_ctrl_6.Enable(False)
        self.choice_6.Enable(False)

    def scan_monthly_schedule(self, event):  # wxGlade: root_frame.<event_handler>
        # print("Event handler 'scan_monthly_schedule' not implemented!")
        # event.Skip()

        # Disable Daily Scan Controls
        self.spin_ctrl_1.Enable(False)
        self.spin_ctrl_7.Enable(False)
        self.choice_4.Enable(False)

        # Disable Weekly Scan Controls
        self.choice_2.Enable(False)
        self.spin_ctrl_3.Enable(False)
        self.spin_ctrl_4.Enable(False)
        self.choice_5.Enable(False)

        # Enable Monthly Scan Controls
        self.choice_3.Enable(True)
        self.spin_ctrl_5.Enable(True)
        self.spin_ctrl_6.Enable(True)
        self.choice_6.Enable(True)

    # def quick_deep_scan(self, event):  # wxGlade: root_frame.<event_handler>
    #     print("Event handler 'quick_deep_scan' not implemented!")
    #     event.Skip()

    def apply_settings(self, event):  # wxGlade: root_frame.<event_handler>
        # print("Event handler 'apply_settings' not implemented!")
        # event.Skip()

        # Identifying which schedule option is selected
        daily_scan_radio = self.radio_btn_1.GetValue()
        weekly_scan_radio = self.radio_btn_2.GetValue()
        monthly_scan_radio = self.radio_btn_3.GetValue()
        # print(daily_scan_radio,weekly_scan_radio,monthly_scan_radio)

        if daily_scan_radio is True:
        # Getting data from Daily Scan options
        	schedule_daily_hour = self.spin_ctrl_1.GetValue()
        	schedule_daily_minutes = self.spin_ctrl_7.GetValue()
        	schedule_daily_ampm = self.choice_4.GetCurrentSelection()
        	f = open("preferences.log","w+")
        	f.write(str(schedule_daily_hour)+" "+str(schedule_daily_minutes)+" "+str(schedule_daily_ampm))
        	f.close()
        	# print(schedule_daily_hour,schedule_daily_minutes,schedule_daily_ampm)
        elif weekly_scan_radio is True:
	        # Getting data from Weekly Scan options
	        schedule_weekly_day = self.choice_2.GetCurrentSelection()
	        schedule_weekly_hour = self.spin_ctrl_3.GetValue()
	        schedule_weekly_minutes = self.spin_ctrl_4.GetValue()
	        schedule_weekly_ampm = self.choice_5.GetCurrentSelection()
	        f = open("preferences.log","w+")
        	f.write(str(schedule_weekly_day)+" "+str(schedule_weekly_hour)+" "+str(schedule_weekly_minutes)+" "+str(schedule_weekly_ampm))
        	f.close()
	        # print(schedule_weekly_day,schedule_weekly_hour,schedule_weekly_minutes,schedule_weekly_ampm)
        elif monthly_scan_radio is True:
	        # Getting data from Monthly Scan options
	        schedule_monthly_day = self.choice_3.GetCurrentSelection()
	        schedule_monthly_hour = self.spin_ctrl_5.GetValue()
	        schedule_monthly_minutes = self.spin_ctrl_6.GetValue()
	        schedule_monthly_ampm = self.choice_6.GetCurrentSelection()
	        f = open("preferences.log","w+")
        	f.write(str(schedule_monthly_day)+" "+str(schedule_monthly_hour)+" "+str(schedule_monthly_minutes)+" "+str(schedule_monthly_ampm))
        	f.close()
	        # print(schedule_monthly_day,schedule_monthly_hour,schedule_monthly_minutes,schedule_monthly_ampm)

    def apply_and_close(self, event):  # wxGlade: root_frame.<event_handler>
        # print("Event handler 'apply_and_close' not implemented!")
        # event.Skip()
        self.apply_settings(event)
        self.Close()

    def realtime_processing(self, event):  # wxGlade: root_frame.<event_handler>
        print("Event handler 'realtime_processing' not implemented!")
        event.Skip()


# end of class root_frame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = root_frame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()