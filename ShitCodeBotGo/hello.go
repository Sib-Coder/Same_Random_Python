package main

import (
	"flag"
	"github.com/go-telegram-bot-api/telegram-bot-api/v5"
	"log"
	"os"
)

// клавиатура
var numericKeyboard = tgbotapi.NewInlineKeyboardMarkup(
	tgbotapi.NewInlineKeyboardRow(
		tgbotapi.NewInlineKeyboardButtonData("vim_master", "vim_master"),
		tgbotapi.NewInlineKeyboardButtonData("Ksusha", "Ksusha"),
	),
	tgbotapi.NewInlineKeyboardRow(
		tgbotapi.NewInlineKeyboardButtonData("4", "4"),
		tgbotapi.NewInlineKeyboardButtonData("5", "5"),
		tgbotapi.NewInlineKeyboardButtonData("6", "6"),
	),
)

var (
	telegramBotToken string
)

func init() {
	// принимаем на входе флаг -telegrambottoken
	flag.StringVar(&telegramBotToken, "telegrambottoken", "", "Telegram Bot Token")
	flag.Parse()

	// без него не запускаемся
	if telegramBotToken == "" {
		log.Print("-telegrambottoken is required")
		os.Exit(1)
	}
}

func main() {

	// используя токен создаем новый инстанс бота
	bot, err := tgbotapi.NewBotAPI(telegramBotToken)
	if err != nil {
		log.Panic(err)
	}

	log.Printf("Authorized on account %s", bot.Self.UserName)

	// u - структура с конфигом для получения апдейтов
	u := tgbotapi.NewUpdate(0)
	u.Timeout = 60

	// используя конфиг u создаем канал в который будут прилетать новые сообщения
	updates := bot.GetUpdatesChan(u)

	// в канал updates прилетают структуры типа Update
	// вычитываем их и обрабатываем
	handle_flag := false
	task := ""
	for update := range updates {
		reply := " "
		if update.Message == nil {
			// Respond to the callback query, telling Telegram to show the user
			// a message with the data received.
			callback := tgbotapi.NewCallback(update.CallbackQuery.ID, update.CallbackQuery.Data)
			if _, err := bot.Request(callback); err != nil {
				panic(err)
				//ЛЮТЫЙ КОСТЫЛЬ В ОТВЕТАХ УЖЕ ПРЕДУСМОТРЕННО!!!
				//	continue
			}

			// And finally, send a message containing the data received.
			if update.CallbackQuery.Data == "vim_master" {
				msg := tgbotapi.NewMessage(update.CallbackQuery.Message.Chat.ID, "Vim Vim Vim. Bash Bash Bash. Попробуйте достать флаг\n ```ssh ctf@192.168.203.3```\n ```sibears```\nВведите флаг")
				if _, err := bot.Send(msg); err != nil {
					panic(err)
				}
				handle_flag = true
				task = update.CallbackQuery.Data
			}

			if update.CallbackQuery.Data == "Ksusha" {
				msg := tgbotapi.NewMessage(update.CallbackQuery.Message.Chat.ID, "Roman Lider - it is my heroy")
				if _, err := bot.Send(msg); err != nil {
					panic(err)
				}
				handle_flag = true
				task = update.CallbackQuery.Data
			}
			continue
		}

		if handle_flag {
			if task == "vim_master" {
				if update.Message.Text == "SiBears{1_r35p3c7_y0u_8r0}" {
					reply = "Correct"
				} else {
					reply = "Incorrect"
				}
			}
			if task == "Ksusha" {
				if update.Message.Text == "roma palkin" {
					reply = "Correct"
				} else {
					reply = "Incorrect"
				}
			}
			msg := tgbotapi.NewMessage(update.Message.Chat.ID, reply)
			msg.ReplyMarkup = numericKeyboard
			// отправляем
			bot.Send(msg)
		}

		//свич на обработку сообщений
		switch update.Message.Text {
		case "sib-coder":
			reply = "Лектор"
		case "барабулька":
			reply = "Хороший парень"
		default:
			// универсальный ответ на любое сообщение
			reply = ""
		}

		// логируем от кого какое сообщение пришло
		log.Printf("[%s] %s", update.Message.From.UserName, update.Message.Text)

		// свитч на обработку комманд
		// комманда - сообщение, начинающееся с "/"
		switch update.Message.Command() {
		case "start":
			reply = "Привет. Я телеграм-бот от команды SiBears. Я рассылаю таски и умею принимать флаги , а так же умею наваливать кринжа"
		case "stop":
			reply = "Пока. До новых встреч)))"
		}

		// создаем ответное сообщение
		msg := tgbotapi.NewMessage(update.Message.Chat.ID, reply)
		msg.ReplyMarkup = numericKeyboard
		// отправляем
		bot.Send(msg)
	}
}
