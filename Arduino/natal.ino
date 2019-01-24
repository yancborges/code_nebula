int luzes[] = {8,9,10,11,12,13};
int botao = 4;
int cont = 0;
int tempo = millis();
int i = 8;
int condicao = 0;


void setup() {
    for(int i = 8; i <= 13; i++){
        pinMode(i, OUTPUT);  
    }

    pinMode(botao, INPUT);

    Serial.begin(9600);
    
}


void loop() {
    if(digitalRead(botao) == HIGH){
        cont ++;
    if(cont >= 4){
        cont = 0;
    }
    
    if(cont == 1){
    
        if(millis()-tempo >= 500) {
            
            if(condicao == 0){
                digitalWrite(i, HIGH);    
            }
            else{
                digitalWrite(i, LOW);  
            }
            
            tempo = millis();
        
        
            if( i > 13){
                i = 8;
                if(condicao == 1){
                    condicao = 0;
                }
                else{
                    condicao = 1;
                }
            }
            
            i++;
        }
    
    }
    else if(cont == 2){
        
        i++;
        
        if(millis()-tempo >= 500) {
            
            if(condicao == 0) {
                digitalWrite(i, HIGH)
            }
            else {
                digitalWrite(i, LOW);
            }
        
            tempo = millis();
        
            if( i > 13) {
                i = 8;
                if(condicao == 0) {
                    condicao++;
                }
                else {
                    condicao = 0;
                }
            }
            
            i++;
        
        }
        
        
    }
    else if(cont == 3){
    
        if(millis()-tempo >= 500) {
            if(condicao == 0) {
                digitalWrite(i, HIGH)
            }
            else {
                digitalWrite(i, LOW);
            }
        
            tempo = millis();
        
            if( i > 13) {
                i = 8;
                if(condicao == 0) {
                    condicao++;
                }
                else {
                    condicao = 0;
                }
            }
            
            i += 2
        }
    
    }
    else {
        
        if(millis()-tempo >= 500) {
            
            if(condicao == 0) {
                if(i/2 == 0) {
                    digitalWrite(i, HIGH)
                }
                else {
                    digitalWrite(i, LOW)
                }
            }
            else {
                if(i/2 == 0) {
                    digitalWrite(i, LOW)
                }
                else {
                    digitalWrite(i, HIGH)
                }
            }
        
            tempo = millis();
        
            if( i > 13) {
                i = 8;
                if(condicao == 0) {
                    condicao++;
                }
                else {
                    condicao = 0;
                }
            }
            
            i++;            
            
        }
    }
  

}
