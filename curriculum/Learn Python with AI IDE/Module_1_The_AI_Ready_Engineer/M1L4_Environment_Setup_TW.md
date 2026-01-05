# Module 1 Lesson 4: 建立實驗室：Virtual Environment (Conda)

> **課程體系：Learn Python with AI IDE**
> **當前模組**：Module 1 - The AI Ready Engineer
> **本課目標**：構建安全、可複現的 Python 開發環境，理解**虛擬環境 (Virtual Environment)** 的隔離本質。

---

## 1. 為什麼不能直接用系統 Python？

想像一下，你的作業系統（Windows/macOS）是一座精密的摩天大樓。
而我們上一課在終端機裡看到的那個 `python`（系統內建），是支撐這座大樓水電系統的**核心基礎設施**。

**為什麼要建立虛擬環境？因為「生化隔離」。**

*   **危險的操作**：作為初學者，你會頻繁安裝各種 AI 套件（numpy, torch）。如果你直接把這些裝在系統 Python 裡，一旦版本衝突，可能會導致系統基礎工具（如 yum, brew 或系統設定）崩潰。
*   **版本打架**：Project A 需要 Python 3.8，Project B 需要 Python 3.12。如果只有一個環境，它們根本無法共存。

**工程化解決方案**：我們在大樓外，搭建一個個獨立的「生化實驗室」 (Sandbox)。
*   **安全**：實驗室炸了也不會影響系統大樓。
*   **獨立**：每個專案一個實驗室，互不干擾。
*   **可丟棄**：環境玩壞了？刪掉重建即可，毫髮無傷。

我們將使用 **Miniconda**，它是業界最成熟、最輕量的環境管理工具。

---

## 2. 準備：驗明正身 (Pre-flight Check)

下載軟體前，必須確認你的硬體架構，否則裝上了也跑不起來。

### 🍎 macOS 用戶
點擊螢幕左上角的 ** -> 關於這台 Mac (About This Mac)**。
*   **Apple M1/M2/M3...**：架構為 **ARM64** (Apple Silicon)。請下載 **macOS Apple Silicon** 版。
*   **Intel Core...**：架構為 **x86_64** (Intel)。請下載 **macOS Intel x86** 版。

### 🪟 Windows 用戶
現代 PC 幾乎全是 **x64** 架構。
*   右鍵「此電腦」 -> 內容 -> 確認「64 位元作業系統，基於 x64 的處理器」。

---

## 3. 安裝：部署 Miniconda

我們推薦 **Miniconda** 而不是 Anaconda。前者只有 50MB（純淨），後者有 600MB（臃腫）。

請前往 [Miniconda 官網下載頁](https://docs.conda.io/en/latest/miniconda.html) 下載對應的安裝包。

### 3.1 Windows 安裝關鍵點 (PATH 策略)
在安裝步驟中，你會看到紅色的警告 *"Add Miniconda3 to my PATH environment variable"*。
*   **新手強烈推薦 (勾選)**：雖然安裝程式可能會嚇唬你，但為了讓你能在 PowerShell 裡直接使用 `conda` 指令，**請務必勾選它**。這會極大地降低新手配置 IDE 的難度。
    *   *注意：如果你電腦裡之前裝過 Anaconda 或其他 Python，建議先移除乾淨再安裝 Miniconda。*

### 3.2 macOS 安裝關鍵點
*   下載 `.pkg` 安裝包，一路「繼續」即可。
*   **重要**：安裝完成後，**必須關閉並重新打開終端機**，才能讓環境變數生效。

---

## 4. 實戰：透過終端機管理環境

打開你的終端機（Mac Terminal / Win PowerShell）。

### 4.1 驗證安裝
輸入：
```bash
conda --version
```
*   **成功訊號**：輸出 `conda 24.x.x` 或類似版本號。
*   **失敗訊號**：`command not found`。
    *   *Mac*：試試執行 `source ~/.zshrc`。
    *   *Windows*：重啟電腦。

### 4.2 建立環境 (Create)
建立我們的第一個實驗室名為 `ai_course`：
```bash
conda create -n ai_course python=3.10 -y
```
*   `-n ai_course`：給實驗室取個名字。
*   `python=3.10`：指定這個實驗室配備 Python 3.10 版本（AI 領域目前最穩定的版本）。

### 4.3 啟用環境 (Activate)
這是最關鍵的一步。環境建好了，你得**進去**。
```bash
conda activate ai_course
```

**觀察終端機變化**：
命令列最左側的提示字元應該從 `(base)` 變成了 **`(ai_course)`**。
*   `(base)`：預設的大廳，不要在這裡裝東西。
*   `(ai_course)`：你的私人實驗室。此時輸入 `python`，呼叫的就是這個盒子裡的 Python。

---

## 5. 跨平台安全策略 (Windows Only)

**Windows 用戶請注意**：PowerShell 預設可能會阻止 `conda` 腳本執行。如果你遇到「禁止執行指令碼」的紅色報錯：

1.  用**管理員身分**執行 PowerShell。
2.  輸入以下「解封」指令：
    ```powershell
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```
3.  輸入 `Y` 並按下 Enter 確認。
4.  關閉管理員視窗，重新打開普通 PowerShell 即可。

---

## 6. 工程自檢 (Engineering Checkpoint)

本課結束，請務必執行以下驗收流程。

### ✅ 驗收標準 (Pass Criteria)
1.  **位置隔離**：在啟用 `(ai_course)` 後，輸入 `which python` (Mac) 或 `where python` (Win)。
    *   **預期**：路徑裡必須包含 `.../envs/ai_course/...`。
    *   *Fail*：如果路徑裡還是 WindowsApps 或者 `/usr/bin/python`，說明你沒啟用成功。
2.  **版本一致**：輸入 `python --version`。
    *   **預期**：必須是 `Python 3.10.x`。
3.  **環境列表**：輸入 `conda env list`，能看到星號 `*` 指向 `ai_course`。

### 🔄 最小重現與重置 (Recovery)
如果你把 `ai_course` 搞壞了，只需利用虛擬環境的「可丟棄」特性：
```bash
# 1. 先退出來
conda deactivate
# 2. 連鍋端刪掉
conda remove -n ai_course --all
# 3. 重新建一個
conda create -n ai_course python=3.10 -y
```

---

> [!IMPORTANT]
> **本課結語**
>
> 現在，我們擁有了一個乾淨、安全、隔離的開發環境。
> 你不再是「裸奔」的游擊隊，而是擁有正規實驗室的科學家。
>
> 既然有了實驗室，我們以後做的實驗（程式碼）也應該被正規地記錄下來，而不是像 REPL 那樣隨手丟棄。
> **下一課：腳本工程 —— 從對話到寫作。**
