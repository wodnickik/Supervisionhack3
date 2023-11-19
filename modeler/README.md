# Modeler

## Zadanie dodatkowe
Przygotowaliśmy model, który na podstawie danych historycznych przewiduje przyszłe oprocentowanie lokaty. Wybraliśmy dane dla banku mBank, ponieważ był to bank z najlepiej udokumentowaną historią oprocentowania. Jako feature'y nasz model wykorzystuje przeszłe oprocentowanie, cenę akcji oraz wolumen akcji mBanku na giełdzie. Dodatkowo jako ostatni feature wykorzystaliśmy stopę bezrobocia. 
Każdy feature został przeprocesowany, tak aby rozkład danej zmiennej był bardziej przystepny dla modelu.

Jako sam model wybraliśmy lekko zmodyfikowany transformer wprowadzony w paperze `Attention is all you need` [vaswani et al. 2017](https://arxiv.org/abs/1706.03762). 
Na dzięn dziejszy jest to model o zdecydowanie największy potencjale, stanowi on podstawę takich aplikacji jak ChatGPT czy Stable Diffusion.
Nasza modyfikacja polegała na zamianie pierwszej warstwy modelu z warsty `Embeddingu`, która jest przystosowana do danych dyskretnych, na warstwę sieci rekurencyjnej `LSTM`, która powinna być wykorzystywana do danych ciągłych.  